# %%
from matterviz.structure import StructureWidget
from matterviz.trajectory import TrajectoryWidget
from pymatgen.core import Lattice, Structure

struct = Structure(  # create dummy structure
    lattice=Lattice.cubic(2.87),
    species=("Fe", "Fe"),
    coords=((0, 0, 0), (0.5, 0.5, 0.5)),
)

print(f"Formula: {struct.formula}")
print(f"Number of sites: {len(struct)}")

struct_widget = StructureWidget(
    structure=struct,
    show_bonds=True,
    atom_radius=0.8,
    color_scheme="Jmol",
)

struct_widget

# %% Create a simple trajectory with two frames
trajectory_data = {
    "frames": [
        {"structure": struct.as_dict(), "metadata": {"step": 0, "energy": -8.2}},
        {
            "structure": Structure(
                lattice=Lattice.cubic(2.90),  # Slightly expanded
                species=("Fe", "Fe"),
                coords=((0, 0, 0), (0.5, 0.5, 0.5)),
            ).as_dict(),
            "metadata": {"step": 1, "energy": -8.1},
        },
    ],
    "metadata": {"temperature": 300},
}

trajectory_widget = TrajectoryWidget(
    trajectory=trajectory_data,
    width=800,
    height=500,
    layout="horizontal",
    display_mode="structure",
)

trajectory_widget
