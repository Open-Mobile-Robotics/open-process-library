Sure, let's update the examples to use "PEA" examples instead of "BMS" examples.

---

# Burroughs Mining Drill Rig Control

This document outlines the best practices for modeling the Drill Rig Control system at the Burroughs Mining Station using the Open Process Library standards. The goal is to provide a clear, consistent approach for representing the control and monitoring of drill rig operations.

- [Type Definition](#type-definition)
- [Type Requirements](#type-requirements)
- Examples
  * [Single Drill Rig](#example-single-drill-rig)
  * [Multi-Drill Rig Operation](#example-multi-drill-rig-operation)
- [Optional and Future Extensions](#optional-and-future-extensions)

## Type Definition
Drill rigs are essential components in mining operations, used for drilling into the earth to extract resources. They typically include components like motors, vibration sensors, and controllers to ensure efficient and safe operation.

## Type Requirements
- It **must** have a motor for drilling.
- It **must** monitor and control the vibration levels.
- It **must** provide feedback on the operational status.
- It **must** handle commands to start and stop the motor.

## Example: Single Drill Rig
This version of a drill rig operates as a stand-alone device in a mining operation.

### PEA Example
![Drill Rig Single](./figures/pea_screenshots/drill_rig_single.png)

### System Diagram and Connections
![Drill Rig Single](./figures/system_diagrams/drill_rig_single.png)

### Sample Configuration
```yaml
BURR_MO:
  type: FACILITIES/MINING_OPERATION

DRILL_RIG_1:
  pol_device_id: 1234
  connections:
    BURR_MO: CONTAINS
  type: MINING/DRILL_RIG
  translation:
    vibration_sensor_feedback:
      present_value: points.vibration_sensor.present_value
      units:
        key: pointset.points.vibration_sensor.units
        values:
          mm_per_sec: mm/s
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

```

## Example: Multi-Drill Rig Operation
This setup includes multiple drill rigs operating within the same mining operation, coordinated for efficiency and safety.

### PEA Example
![Drill Rig Multi](./figures/pea_screenshots/drill_rig_multi.png)

### System Diagram and Connections
![Drill Rig Multi](./figures/system_diagrams/drill_rig_multi.png)

### Sample Configuration
```yaml
BURR_MO:
  type: FACILITIES/MINING_OPERATION

DRILL_RIG_1:
  pol_device_id: 1234
  connections:
    BURR_MO: CONTAINS
  type: MINING/DRILL_RIG
  translation:
    vibration_sensor_feedback:
      present_value: points.vibration_sensor.present_value
      units:
        key: pointset.points.vibration_sensor.units
        values:
          mm_per_sec: mm/s
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

DRILL_RIG_2:
  pol_device_id: 2345
  connections:
    BURR_MO: CONTAINS
  type: MINING/DRILL_RIG
  translation:
    vibration_sensor_feedback:
      present_value: points.vibration_sensor.present_value
      units:
        key: pointset.points.vibration_sensor.units
        values:
          mm_per_sec: mm/s
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

```

## Optional and Future Extensions
This section contains additional features and extensions that could be added in the future.
- Advanced monitoring capabilities for predictive maintenance.
- Integration with other mining operation systems for enhanced automation.
- Adding more detailed control options for complex drilling operations.

**Note:** All PEA screenshots taken from the hypothetical Burroughs Mining Station control system.