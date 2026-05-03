# Notebook 02 Summary — Global vs Local Tile Capture

Notebook 02 compares one single-lane detector against a full local tile union.

## Result

- Target persisting Mod30 lanes: `[1, 7, 11, 13, 17, 19, 23, 29]`
- Single-lane detector captures: `[np.int64(1)]`
- Single-lane detector misses: `[7, 11, 13, 17, 19, 23, 29]`
- Single-lane coverage: `0.125`
- Local tile union coverage: `1.000`

## Interpretation

A single interpretable feature can be structurally incomplete.
A tiled representation preserves persisting structure by distributing capture across local residue lanes.

## Generated files

- `figures/06_global_vs_tiled_lane_coverage.png`
- `figures/07_single_lane_capture.png`
- `figures/08_tiled_capture_preserves_structure.png`
- `figures/09_detector_map_over_residues.png`
- `data/02_global_vs_tiled_coverage.csv`
- `data/02_residue_capture_map.csv`
