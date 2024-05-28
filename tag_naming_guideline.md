## Not Accepted - Draft Tag Naming Guideline

### Harmonized PLC Tag Naming Guideline for Process Automation (Aligned with ISA 5.1)

---

### General Structure

```
<Plant/Area>_<System>_<Subsystem>_<PEA>_<Equipment/Instrument>_<Attribute>_<Qualifier>
```

### Components of the Tag Naming Structure

1. **Plant/Area**: Identifies the specific plant or area within the plant.
2. **System**: Specifies the system to which the equipment belongs (e.g., Process, Utility).
3. **Subsystem**: Further refines the system category (e.g., Reactor, Boiler).
4. **PEA**: Identifies the Process Equipment Assembly.
5. **Equipment/Instrument**: Denotes the specific equipment or instrument (e.g., Valve, Pump, Sensor).
6. **Attribute**: Describes the attribute or parameter of the equipment/instrument (e.g., Status, Command, Feedback).
7. **Qualifier**: Provides additional context or details about the attribute (e.g., Current, Setpoint, Error).

### Detailed Tag Naming Components

#### 1. Plant/Area
- **Guideline**: Use a short, unique identifier for each plant or area. Ensure identifiers are consistent and well-documented.
- **Example**: `P1` for Plant 1, `A1` for Area 1.

#### 2. System
- **Guideline**: Use a standard abbreviation for each system. Follow ISA-5.1 standards for instrumentation symbols and identification.
- **Example**: `PROC` (Process), `UTIL` (Utility).

#### 3. Subsystem
- **Guideline**: Use a standard abbreviation for each subsystem. Ensure subsystems are logically grouped and easily identifiable.
- **Example**: `RX` (Reactor), `BLR` (Boiler).

#### 4. PEA (Process Equipment Assembly)
- **Guideline**: Use a descriptive name or abbreviation for the Process Equipment Assembly. Ensure it reflects the function or type of the assembly.
- **Example**: `COOL` (Cooling System), `FEED` (Feed System).

#### 5. Equipment/Instrument
- **Guideline**: Use a descriptive name or abbreviation for the equipment/instrument. Follow ISA-5.1 for instrumentation symbols and naming conventions.
- **Example**: `FV` (Flow Valve), `TT` (Temperature Transmitter), `PT` (Pressure Transmitter).

#### 6. Attribute
- **Guideline**: Use a standard abbreviation for the attribute. Attributes should clearly define the data type or control action.
- **Example**: `STS` (Status), `CMD` (Command), `FB` (Feedback).

#### 7. Qualifier
- **Guideline**: Use a qualifier to provide additional detail if necessary. Qualifiers should be used to enhance clarity and specificity.
- **Example**: `CURR` (Current), `SP` (Setpoint), `ERR` (Error).

### Example Tag Naming Convention

#### Valve in a Reactor Cooling System within a PEA
- **Plant/Area**: `P1` (Plant 1)
- **System**: `PROC`
- **Subsystem**: `RX` (Reactor)
- **PEA**: `COOL` (Cooling System)
- **Equipment/Instrument**: `FV` (Flow Valve)
- **Attribute**: `STS` (Status)
- **Qualifier**: `CURR` (Current)

**Tag**: `P1_PROC_RX_COOL_FV_STS_CURR`

#### Sensor in a Utility Boiler System within a PEA
- **Plant/Area**: `P2` (Plant 2)
- **System**: `UTIL`
- **Subsystem**: `BLR` (Boiler)
- **PEA**: `FEED` (Feed System)
- **Equipment/Instrument**: `TT` (Temperature Transmitter)
- **Attribute**: `FB` (Feedback)
- **Qualifier**: `TEMP` (Temperature)

**Tag**: `P2_UTIL_BLR_FEED_TT_FB_TEMP`

### Harmonization Principles

1. **Clarity**: Ensure that each tag name clearly represents the associated equipment and attribute, avoiding ambiguity.
2. **Consistency**: Use standard abbreviations and structures across all tags to maintain consistency.
3. **Scalability**: Design the tag structure to accommodate future expansions and modifications without major changes.
4. **Usability**: Ensure that tags are easily readable and interpretable by operators, engineers, and maintenance personnel.
5. **Integration**: Align with industry standards and practices, such as ISA-5.1, ISA-88, ISA-95, and MTP, to facilitate integration and interoperability with other systems.
6. **Modularity**: Utilize modular naming conventions that reflect the hierarchical and reusable nature of PEAs in process automation.

# Tag Naming Best Practices (Harmonized with ISA 5.1)

## Overview
This document outlines best practices for tag naming conventions in automation systems, integrating guidelines from ISA-95 standards, the Google Digital Buildings Ontology, and the MTP (Module Type Package) standard. Examples are inspired by the systems and sensors found in the "Red Mars" series.

## General Principles
- **Consistency**: Use a consistent naming convention across all tags.
- **Clarity**: Tag names should be clear and descriptive.
- **Scalability**: The naming convention should support the addition of new tags without ambiguity.
- **Hierarchy**: Use hierarchical naming to reflect the structure and relationships of components.

## Tag Structure
The recommended structure for tag names is as follows:

```
<Plant/Area>_<System>_<Subsystem>_<PEA>_<Equipment/Instrument>_<Attribute>_<Qualifier>
```

### ISA-95 Levels
- **Plant/Area**: The highest organizational level within the site.
- **System**: A specific system within the plant.
- **Subsystem**: A major division within the system.
- **PEA**: Process Equipment Assembly, representing a functional unit within the process.

### PEA Elements (Based on MTP Standard)
- **Equipment/Instrument**: Represents individual pieces of equipment within the PEA.
- **Attribute**: The lowest level of detail for the equipment/instrument, indicating specific parameters or statuses.

### Fields and Subfields (Based on Google Digital Buildings Ontology)
The fields are constructed from specific subfields to provide detailed information about the data point or parameter.

#### Subfields and Field Construction

| Subfield      | Description                                   | Example               |
|---------------|-----------------------------------------------|-----------------------|
| Sensor        | Indicates the type of sensor                  | `TempSensor`          |
| Parameter     | Specific parameter measured or controlled     | `Temperature`         |
| Status        | Indicates the operational status              | `Status`              |
| Setpoint      | Desired value for control                     | `Setpoint`            |
| CurrentValue  | Actual value measured                         | `CurrentValue`        |
| Command       | Control command to be executed                | `Start`               |
| Alarm         | Indicates an alarm condition                  | `HighAlarm`           |
| Mode          | Operating mode of the equipment               | `AutoMode`            |
| State         | Current state of the equipment                | `RunningState`        |

#### Field Examples

| Field                              | Description                                              |
|------------------------------------|----------------------------------------------------------|
| `TempSensor_Temperature`           | Temperature measured by a temperature sensor             |
| `TempSensor_Temperature_Setpoint`  | Desired temperature setpoint                             |
| `TempSensor_Temperature_CurrentValue` | Current temperature value measured by the sensor       |
| `Pump_Status`                      | Operational status of the pump                           |
| `Pump_Start_Command`               | Command to start the pump                                |
| `Pump_HighAlarm`                   | High alarm condition for the pump                        |
| `Pump_AutoMode`                    | Automatic operating mode of the pump                     |
| `Pump_RunningState`                | Current running state of the pump                        |

### PEA (Process Equipment Assembly) Objects
PEA elements consist of common objects necessary for process control and automation.

| Object            | Description                                                        |
|-------------------|--------------------------------------------------------------------|
| Equipment/Instrument   | A functional unit within the process, such as a pump or a heater   |
| ControlModule     | The control unit for an equipment module, such as a valve or sensor|
| Parameter         | Specific parameters controlled or measured                         |
| Setpoint          | Desired target values for control                                  |
| Status            | Operational status of equipment                                    |
| Command           | Control commands for operation                                     |
| Alarm             | Alarm conditions and thresholds                                    |
| Mode              | Operating modes of the equipment                                   |
| State             | Operational states of the equipment                                |

### Alarms, States, and Modes (Based on ISA-18.2)

#### Alarm Management
- **Alarm Tag Naming**: Use a clear and descriptive naming convention for alarms to ensure they are easily identifiable.
- **Examples**:
  - `P1_PROC_HYDP_PS1_PUMP1_Flow_HighAlarm`
  - `P1_ATMOS_A2_SCRS1_SCR1_CO2_HighAlarm`

| Alarm Type      | Description                                     | Example                              |
|-----------------|-------------------------------------------------|--------------------------------------|
| High Alarm      | Indicates a high-level condition                | `HighFlowAlarm`                      |
| Low Alarm       | Indicates a low-level condition                 | `LowFlowAlarm`                       |
| High-High Alarm | Indicates a critical high-level condition       | `HighHighPressureAlarm`              |
| Low-Low Alarm   | Indicates a critical low-level condition        | `LowLowPressureAlarm`                |
| Fault Alarm     | Indicates a fault condition in the equipment    | `PumpFaultAlarm`                     |

#### State Management
- **State Tag Naming**: Use descriptive names for equipment states to track operational status.
- **Examples**:
  - `P1_HYDP_PS1_PUMP1_RunningState`
  - `P1_ATMOS_A2_SCRS1_SCR1_IdleState`

| State Type      | Description                                       | Example                              |
|-----------------|---------------------------------------------------|--------------------------------------|
| Running         | Indicates the equipment is operating              | `RunningState`                       |
| Idle            | Indicates the equipment is idle                   | `IdleState`                          |
| Fault           | Indicates the equipment is in a fault condition   | `FaultState`                         |
| Maintenance     | Indicates the equipment is under maintenance      | `MaintenanceState`                   |

#### Mode Management
- **Mode Tag Naming**: Use descriptive names for operating modes to control and monitor the equipment.
- **Examples**:
  - `P1_HYDP_PS1_PUMP1_AutoMode`
  - `P1_ATMOS_A2_SCRS1_SCR1_ManualMode`

| Mode Type       | Description                                       | Example                              |
|-----------------|---------------------------------------------------|--------------------------------------|
| Auto            | Automatic operating mode                         | `AutoMode`                           |
| Manual          | Manual operating mode                            | `ManualMode`                         |
| Maintenance     | Maintenance operating mode                       | `MaintenanceMode`                    |

## Examples Inspired by "Red Mars" Series

### Hydronic Systems
- **Water Pump Control**:
  - `P1_HYDP_PS1_PUMP1_Start_Command`
  - `P1_HYDP_PS1_PUMP1_FlowRate_CurrentValue`
  - `P1_HYDP_PS1_PUMP1_FlowRate_Setpoint`
  - `P1_HYDP_PS1_PUMP1_HighFlowAlarm`
  - `P1_HYDP_PS1_PUMP1_RunningState`
  - `P1_HYDP_PS1_PUMP1_AutoMode`

### Atmospheric Control
- **Air Scrubber Control**:
  - `P1_ATMOS_A2_SCRS1_SCR1_Start_Command`
  - `P1_ATMOS_A2_SCRS1_SCR1_CO2Level_CurrentValue`
  - `P1_ATMOS_A2_SCRS1_SCR1_CO2Level_Setpoint`
  - `P1_ATMOS_A2_SCRS1_SCR1_CO2HighAlarm`
  - `P1_ATMOS_A2_SCRS1_SCR1_RunningState`
  - `P1_ATMOS_A2_SCRS1_SCR1_AutoMode`

### Energy Management
- **Solar Panel Monitoring**:
  - `P1_ENRG_A1_SOLST1_PANEL1_PowerOutput_CurrentValue`
  - `P1_ENRG_A1_SOLST1_PANEL1_Status`
  - `P1_ENRG_A1_SOLST1_PANEL1_Angle_Setpoint`
  - `P1_ENRG_A1_SOLST1_PANEL1_LowPowerAlarm`
  - `P1_ENRG_A1_SOLST1_PANEL1_RunningState`
  - `P1_ENRG_A1_SOLST1_PANEL1_AutoMode`

### Agriculture
- **Greenhouse Environment Control**:
  - `P1_AGR_A3_GRH1_Temperature_CurrentValue`
  - `P1_AGR_A3_GRH1_Temperature_Setpoint`
  - `P1_AGR_A3_GRH1_Humidity_CurrentValue`
  - `P1_AGR_A3_GRH1_HighTempAlarm`
  - `P1_AGR_A3_GRH1_RunningState`
  - `P1_AGR_A3_GRH1_AutoMode`

## Harmonization with MQTT/Zenoh and OPC UA

### MQTT/Zenoh Namespaces

- Use the same tag naming convention to create hierarchical namespaces in MQTT and Zenoh.
- **Examples**:
  - `P1/Hydroponics/PS1/Pump1/FlowRate/CurrentValue`
  - `P1/Atmosphere/SCRS1/Scrubber1/CO2Level/CurrentValue`

### OPC UA Types and Entities
- Define OPC UA nodes and variables using the same naming convention.
- **Examples**:
  - `Objects/P1/Hydroponics/PS1/Pump1/FlowRate/CurrentValue`
  - `Objects/P1/Atmosphere/SCRS1/Scrubber1/CO2Level/CurrentValue`

## Conclusion
Adhering to these best practices will ensure that your tag naming convention is consistent, clear, and scalable, supporting efficient system management and integration across MQTT/Zenoh, OPC UA, and other protocols.