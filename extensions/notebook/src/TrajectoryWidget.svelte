<!--
  MatterViz Trajectory Widget using @anywidget/svelte bindings

  This component receives reactive model bindings from anywidget and passes
  them through to the main Trajectory component from the parent project.
-->
<script>
  import Trajectory from '../../../src/lib/trajectory/Trajectory.svelte'

  /** @type {{ bindings: import('./types.js').TrajectoryBindings }} */
  let { bindings } = $props()

  // Transform bindings into the props format expected by Trajectory.svelte
  let trajectory_props = $derived({
    // Core trajectory data
    trajectory: bindings.trajectory,
    current_step_idx: bindings.current_step_idx,

    // Layout and display
    layout: bindings.layout,
    display_mode: bindings.display_mode,
    show_controls: bindings.show_controls,
    show_fullscreen_button: bindings.show_fullscreen_button,

    // Widget configuration
    width: bindings.width,
    height: bindings.height,
    allow_file_drop: false, // Disable file drop in notebook context

    // Structure properties for embedded Structure component
    structure_props: {
      scene_props: {
        atom_radius: bindings.atom_radius,
        show_atoms: bindings.show_atoms,
        auto_rotate: bindings.auto_rotate,
        same_size_atoms: bindings.same_size_atoms,
        show_bonds: bindings.show_bonds,
        show_force_vectors: bindings.show_force_vectors,
        force_vector_scale: bindings.force_vector_scale,
        force_vector_color: bindings.force_vector_color,
      },
      lattice_props: {
        cell_edge_opacity: bindings.cell_edge_opacity,
        cell_surface_opacity: bindings.cell_surface_opacity,
        cell_edge_color: bindings.cell_edge_color,
        cell_surface_color: bindings.cell_surface_color,
        cell_line_width: bindings.cell_line_width,
        show_vectors: bindings.show_vectors,
      },
      show_site_labels: bindings.show_site_labels,
      show_image_atoms: bindings.show_image_atoms,
      color_scheme: bindings.color_scheme,
      background_color: bindings.background_color,
      background_opacity: bindings.background_opacity,
    },

    // Step labels
    step_labels: bindings.step_labels,
  })
</script>

<!-- Pass through to the main Trajectory component -->
<Trajectory {...trajectory_props} />
