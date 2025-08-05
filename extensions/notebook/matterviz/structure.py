"""Structure visualization widget for Jupyter notebooks."""

from __future__ import annotations

from pathlib import Path
from typing import TYPE_CHECKING, Any

import anywidget
import traitlets as tl

if TYPE_CHECKING:
    from typing import Any as AnyType

# Read the bundled frontend code
_STATIC_DIR = Path(__file__).parent / "static"


class StructureWidget(anywidget.AnyWidget):
    """Interactive structure visualization widget for Jupyter notebooks.

    This widget wraps the MatterViz Structure.svelte component for use in
    Jupyter notebooks and other anywidget-compatible environments.

    Examples:
        Basic usage:
        >>> from matterviz import StructureWidget
        >>> structure_data = {...}  # Structure dictionary from pymatgen/ASE
        >>> widget = StructureWidget(structure=structure_data)
        >>> widget

        With custom visualization options:
        >>> widget = StructureWidget(
        ...     structure=structure_data,
        ...     atom_radius=0.8,
        ...     show_bonds=True,
        ...     color_scheme="Jmol"
        ... )
    """

    _esm = (_STATIC_DIR / "structure.js").read_text()
    _css = (_STATIC_DIR / "structure.css").read_text()

    # Core structure data
    structure = tl.Dict(allow_none=True).tag(sync=True)

    # Scene visualization properties
    atom_radius = tl.Float(1.0).tag(sync=True)
    show_atoms = tl.Bool(True).tag(sync=True)
    show_bonds = tl.Bool(False).tag(sync=True)
    show_site_labels = tl.Bool(False).tag(sync=True)
    show_image_atoms = tl.Bool(True).tag(sync=True)
    show_force_vectors = tl.Bool(False).tag(sync=True)
    same_size_atoms = tl.Bool(False).tag(sync=True)
    auto_rotate = tl.Float(0.0).tag(sync=True)

    # Force vector properties
    force_vector_scale = tl.Float(1.0).tag(sync=True)
    force_vector_color = tl.Unicode("#ff6b6b").tag(sync=True)

    # Bond properties
    bond_thickness = tl.Float(0.1).tag(sync=True)
    bond_color = tl.Unicode("#666666").tag(sync=True)
    bonding_strategy = tl.Unicode("nearest_neighbor").tag(sync=True)

    # Cell/lattice properties
    cell_edge_opacity = tl.Float(0.8).tag(sync=True)
    cell_surface_opacity = tl.Float(0.1).tag(sync=True)
    cell_edge_color = tl.Unicode("#333333").tag(sync=True)
    cell_surface_color = tl.Unicode("#333333").tag(sync=True)
    cell_line_width = tl.Float(2.0).tag(sync=True)
    show_vectors = tl.Bool(True).tag(sync=True)

    # Visual styling
    color_scheme = tl.Unicode("Vesta").tag(sync=True)
    background_color = tl.Unicode(allow_none=True).tag(sync=True)
    background_opacity = tl.Float(0.1).tag(sync=True)

    # Widget dimensions
    width = tl.Int(600).tag(sync=True)
    height = tl.Int(500).tag(sync=True)

    # UI controls
    show_controls = tl.Bool(True).tag(sync=True)
    show_info = tl.Bool(True).tag(sync=True)
    show_fullscreen_button = tl.Bool(True).tag(sync=True)

    # Export settings
    png_dpi = tl.Int(150).tag(sync=True)

    def __init__(
        self,
        structure: dict[str, Any] | AnyType | None = None,
        **kwargs: Any,
    ) -> None:
        """Initialize the StructureWidget.

        Args:
            structure: Structure data (dict from pymatgen/ASE .as_dict() or similar)
            **kwargs: Additional widget properties
        """
        # Convert pymatgen Structure to dict if needed
        if structure is not None and hasattr(structure, "as_dict"):
            structure = structure.as_dict()

        super().__init__(structure=structure, **kwargs)
