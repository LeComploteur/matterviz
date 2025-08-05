<!--
  MatterViz Structure Widget using @anywidget/svelte bindings

  This component receives reactive model bindings from anywidget and passes
  them through to the main Structure component from the parent project.
-->
<script>
  import Structure from '../../../src/lib/structure/Structure.svelte'

  /** @type {{ bindings: import('./types.js').StructureBindings }} */
  let { bindings } = $props()

  // Transform bindings into the props format expected by Structure.svelte
  let structure_props = $derived({
    // Core structure data
    structure: bindings.structure,

    // Scene visualization properties
    scene_props: {
      atom_radius: bindings.atom_radius,
      show_atoms: bindings.show_atoms,
      auto_rotate: bindings.auto_rotate,
      same_size_atoms: bindings.same_size_atoms,
      show_bonds: bindings.show_bonds,
      show_force_vectors: bindings.show_force_vectors,
      force_vector_scale: bindings.force_vector_scale,
      force_vector_color: bindings.force_vector_color,
      bond_thickness: bindings.bond_thickness,
      bond_color: bindings.bond_color,
      bonding_strategy: bindings.bonding_strategy,
    },

    // Lattice properties
    lattice_props: {
      cell_edge_opacity: bindings.cell_edge_opacity,
      cell_surface_opacity: bindings.cell_surface_opacity,
      cell_edge_color: bindings.cell_edge_color,
      cell_surface_color: bindings.cell_surface_color,
      cell_line_width: bindings.cell_line_width,
      show_vectors: bindings.show_vectors,
    },

    // Display options
    show_site_labels: bindings.show_site_labels,
    show_image_atoms: bindings.show_image_atoms,
    color_scheme: bindings.color_scheme,
    background_color: bindings.background_color,
    background_opacity: bindings.background_opacity,

    // Widget configuration
    width: bindings.width,
    height: bindings.height,
    show_buttons: bindings.show_controls,
    enable_info_panel: bindings.show_info,
    fullscreen_toggle: bindings.show_fullscreen_button,
    allow_file_drop: false, // Disable file drop in notebook context
    png_dpi: bindings.png_dpi,
  })
</script>

<!-- Pass through to the main Structure component -->
<Structure {...structure_props} />
