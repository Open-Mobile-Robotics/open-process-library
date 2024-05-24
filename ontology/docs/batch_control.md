Sure, here’s the equivalent Open Process Library document for Material Batch Control in a mining system based on the provided Meter Load Designation document structure:

---

# Material Batch Control (MBC)

This document outlines the best practices for modeling material batch control systems in the Burroughs Mining Station using the Open Process Library standards. The goal is to provide a clear, consistent approach for representing batch processes and their control.

- [Type Definition](#type-definition)
- [Type Requirements](#type-requirements)
- Examples
  * [Material Batch Control System](#example-material-batch-control-system)

## Type Definition
Material batch control systems (MBC) are used in the mining industry to manage the extraction, processing, and handling of material batches. These systems typically include various components such as batch reactors, mixers, conveyors, and other related equipment. The system is designed to handle specific batch operations according to predefined recipes and control strategies.

## Type Requirements
- It **must** include at least one batch reactor.
- It **must** include at least one mixer.
- It **must** provide feedback on the operational status of its components.
- It **must** handle commands to start and stop key components.

## Example: Material Batch Control System

This version of the material batch control system includes variable speed components for batch processing and handling.

### PEA Example
![Material Batch Control System](./figures/pea_screenshots/material_batch_control.png)

### System Diagram and Connections
![Material Batch Control System](./figures/system_diagrams/material_batch_control.png)

### Sample Configuration
```yaml
# Define the facility and the material batch control system.
BURR_MBC:
  type: FACILITIES/MATERIAL_BATCH_CONTROL

# Define the batch reactor and connect it to the system.
BATCH_REACTOR_1:
  pol_device_id: 1234
  connections:
    BURR_MBC: HAS_PART
  type: MINING/BATCH_REACTOR
  translation:
    temperature_sensor_feedback:
      present_value: points.temperature_sensor.present_value
      units:
        key: pointset.points.temperature_sensor.units
        values:
          degrees_celsius: degC
    mixer_speed_command:
      present_value: points.mixer_speed_command.present_value
      units:
        key: pointset.points.mixer_speed_command.units
        values:
          rpm: rpm
    operational_status_feedback:
      present_value: points.operational_status.present_value
      units:
        key: pointset.points.operational_status.units
        values:
          status: st
    ...

# Define the mixer and connect it to the system.
MIXER_1:
  pol_device_id: 2345
  connections:
    BURR_MBC: HAS_PART
  type: MINING/MIXER
  translation:
    speed_sensor_feedback:
      present_value: points.speed_sensor.present_value
      units:
        key: pointset.points.speed_sensor.units
        values:
          rpm: rpm
    motor_command_start:
      present_value: points.motor_start_command.present_value
      units:
        key: pointset.points.motor_start_command.units
        values:
          boolean: bool
    controller_status_feedback:
      present_value: points.controller_status.present_value
      units:
        key: pointset.points.controller_status.units
        values:
          status: st
    ...

# Define the conveyor belt and connect it to the system.
CONV_BELT_1:
  pol_device_id: 3456
  connections:
    BURR_MBC: HAS_PART
  type: MINING/CONVEYOR_BELT
  translation:
    speed_sensor_feedback:
      present_value: points.speed_sensor.present_value
      units:
        key: pointset.points.speed_sensor.units
        values:
          meters_per_second: m/s
    motor_command_start:
      present_value: points.motor_start_command.present_value
      units:
        key: pointset.points.motor_start_command.units
        values:
          boolean: bool
    controller_status_feedback:
      present_value: points.controller_status.present_value
      units:
        key: pointset.points.controller_status.units
        values:
          status: st
    ...

# Define additional equipment served by the material batch control system.
HOPPER_1:
  pol_device_id: 4567
  connections:
    BURR_MBC: FEEDS
  type: MINING/HOPPER
  translation:
    material_level_sensor:
      present_value: points.material_level_sensor.present_value
      units:
        key: pointset.points.material_level_sensor.units
        values:
          meters: m
    discharge_command:
      present_value: points.discharge_command.present_value
      units:
        key: pointset.points.discharge_command.units
        values:
          boolean: bool
    ...

CRUSHER_1:
  pol_device_id: 5678
  connections:
    BURR_MBC: FEEDS
  type: MINING/CRUSHER
  translation:
    operational_status:
      present_value: points.operational_status.present_value
      units:
        key: pointset.points.operational_status.units
        values:
          status: st
    start_command:
      present_value: points.start_command.present_value
      units:
        key: pointset.points.start_command.units
        values:
          boolean: bool
    ...

```

**Note:** All PEA screenshots taken from the hypothetical Burroughs Mining Station control system.

---

This document provides a structured approach to modeling the Burroughs Material Batch Control System using the Open Process Library standards. By following these guidelines, we ensure consistency, clarity, and efficiency in our models.