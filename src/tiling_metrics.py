def lane_density(nums, mod=30):
    lanes = {}
    for n in nums:
        r = n % mod
        lanes[r] = lanes.get(r, 0) + 1
    total = len(nums)
    return {k: v/total for k, v in lanes.items()}

def feature_usage_diagnostics(Z, align, useful_threshold=0.45, activity_eps=1e-6):
    import numpy as np

    feature_activity = np.sum(Z > activity_eps, axis=0)
    active_mask = feature_activity > 0
    dead_mask = ~active_mask

    purity = align.max(axis=1) if align.size else np.zeros(Z.shape[1])

    useful_mask = active_mask & (purity >= useful_threshold)
    redundant_mask = active_mask & (purity < useful_threshold)

    latent_dim = Z.shape[1]

    return {
        "feature_activity": feature_activity,
        "feature_purity": purity,
        "active_features": int(active_mask.sum()),
        "dead_features": int(dead_mask.sum()),
        "useful_features": int(useful_mask.sum()),
        "redundant_features": int(redundant_mask.sum()),
        "active_feature_fraction": float(active_mask.sum() / latent_dim) if latent_dim else 0.0,
        "dead_feature_fraction": float(dead_mask.sum() / latent_dim) if latent_dim else 0.0,
        "useful_feature_fraction": float(useful_mask.sum() / latent_dim) if latent_dim else 0.0,
        "redundant_feature_fraction": float(redundant_mask.sum() / latent_dim) if latent_dim else 0.0,
    }
