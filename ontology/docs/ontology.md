# Open Process Library Ontology

The Open Process Library Ontology defines both [semantic data](https://en.wikipedia.org/wiki/Semantic_data_model) primitives and concrete constructions of these primitives to model physical processes and equipment. The sections below outline the conceptual model of the ontology.

*   For an explanation of the existing abstract model see [model](model.md).
*   For an explanation of the model configuration files see [config](ontology_config.md).

- [Open Process Library Ontology](#open-process-library-ontology)
  * [Overview](#overview)
  * [Namespaces](#namespaces)
  * [Components](#components)
    + [Subfields](#subfields)
    + [Fields](#fields)
      - [Equivalence](#equivalence)
      - [Namespace Elevation](#namespace-elevation)
      - [Enumeration](#enumeration)
      - [Structural Flexibility and Ambiguity](#structural-flexibility-and-ambiguity)
      - [Implicit Inheritance](#implicit-inheritance)
      - [Alternate Approaches and Future Extensions](#alternate-approaches-and-future-extensions)
        * [Equipment Composition](#equipment-composition)
        * [Display Name](#display-name)
    + [Dimensional Units](#dimensional-units)
    + [Multi-State Values](#multi-state-values)
      - [Individual States](#individual-states)
      - [Multi-State Groups](#multi-state-groups)
      - [Effect on Namespace Elevation](#effect-on-namespace-elevation)
    + [Entity Types](#entity-types)
      - [GUIDs](#guids)
      - [Type Names](#type-names)
      - [Field Definitions](#field-definitions)
      - [Inheritance](#inheritance)
      - [Abstract Types](#abstract-types)
      - [Canonical Types](#canonical-types)
      - [Relationship Constraints](#relationship-constraints)
    + [Relationships](#relationships)
    + [Change Management](#change-management)
    + [Notes](#notes)

## Overview

The Open Process Library project is concerned with modeling the characteristics and telemetry of **entities**, and their relationships with each other. An entity is any instance of a "thing" in the model; for example, a plant, a unit, or a piece of equipment (like a pump). The ontology is concerned with "describing the thing."

The ontology describes entities using **entity types**. An entity type indicates both a place within the ontology's composable taxonomy and a set of semantically defined data **fields** that are expected for that entity. Fields are composed of structured groupings of **subfields** that provide them with specific meaning.

Relationships between entities are defined by directed, named **connections**.

Other components of the model stack, such as translations and links, are discussed in [onboarding](building_config.md).

## Namespaces

All elements of the ontology are organized into namespaces, with some constraints. There is a global namespace that all other namespaces can reference directly. Below the global namespace, the ontology allows exactly one level of additional namespaces. Hierarchical namespacing is explicitly disallowed. In the interest of cross-compatibility, certain components are elevated to the global namespace when possible (more details on this in individual component sections).

## Components

### Subfields

The subfield is the basic unit of meaning in the ontology. Each subfield consists of a single or compounded word[^5] with a very specific human-readable definition. Subfields are largely analogous to the concept of a "tag" in Brick or Haystack, but with a few more constraints.

Subfields have the following attributes:

*   Subfields are typically globally defined (i.e., defined in the global namespace).
*   Subfields must be unique within their namespace (typically the global namespace).
*   Each subfield has a unique and specific meaning.
*   Subfield names may be camelCased for readability, but are not case-sensitive.
*   Subfields should be used nearly universally across different namespaces and applications.
*   Subfields cannot be referred to with a namespace identifier (e.g., PROCESS/subfield is not a valid reference).
*   Subfields are grouped into categories that dictate their grouping with each other when they are combined into sets to form fields.

There is no explicit namespacing for subfields, so an individual field's namespace can only use one definition of a subfield.[^6] It is expected that the vast majority of subfields will be defined in the global namespace. Defining a subfield locally prevents any field using it from being elevated to the global namespace.[^7]

Subfields are grouped into categories that add structure to field composition (note that the ordering of this table reflects the expected ordering of subfields in field construction).

<table>
  <tr>
   <td><strong>Category</strong></td>
   <td><strong>Description</strong></td>
   <td><strong>Examples</strong></td>
   <td><strong>Allowed Per Field</strong></td>
   <td><strong>Required</strong></td>
  </tr>
  <tr>
   <td><p style="text-align: right">Aggregation Descriptor</p></td>
   <td>
     A subfield that modifies aggregations to explicitly differentiate temporal aggregation (e.g., daily max) from spatial aggregation (e.g., the max of 3 flow sensors in a unit). Note that windowing specifics are added into this subfield, and omitting them implies a fixed window (e.g., the max over the day boundary if `daily` is used). (Note: the window time is always spelled out to avoid subfield validation errors.) This subfield can only be used when accompanied by an aggregation subfield.
   </td>
   <td>daily, fivesecond, fivesecondrolling</td>
   <td>1</td>
   <td>Optional (Required if Aggregation is used)</td>
  </tr>
  <tr>
   <td><p style="text-align: right">Aggregation</p></td>
   <td>
     An aggregation such as minimum, maximum, rootmeansquare, etc. It is implied that aggregations are spatial (e.g., the max of 3 flow sensors in a unit) except when accompanied by a defined aggregation descriptor. In any case, this is not the same as an operating limit (e.g., the max flowrate for a valve); these are treated separately (see note below).
   </td>
   <td>Average, Max, Min</td>
   <td>1</td>
   <td>Optional</td>
  </tr>
  <tr>
   <td><p style="text-align: right">Descriptor</p></td>
   <td>General purpose modifier that specifies the exact function of the field within the context of the entity. The number of descriptors used should be limited by the context (i.e., if a descriptor is extraneous it should be omitted).
   </td>
   <td>Discharge, Return, Zone, Primary, Chilled etc...</td>
   <td>10</td>
   <td>Optional</td>
  </tr>
  <tr>
   <td><p style="text-align: right">Component</p></td>
   <td>Specifies the specific subcomponent of the entity being represented (e.g., the valve of a valve assembly). As with descriptors, context drives necessity; supply_valve_position_command is necessary for an assembly because there will routinely be an exhaust_valve_position_command that it needs to be distinguished from, but it is clear from the context of a valve that position_command applies to the valve, and therefore no component subfield is necessary to describe it.
</td>
   <td>Valve, pump, compressor...</td>
   <td>10</td>
   <td>Optional</td>
  </tr>
  <tr>
   <td><p style="text-align: right">Measurement Descriptor</p></td>
   <td>
     A modifier of the measurement which adds necessary context. The classic example of this is pressure, which must be distinguished between differential and absolute.
   </td>
   <td>Differential, relative, static</td>
   <td>1</td>
   <td>Optional</td>
  </tr>
  <tr>
   <td><p style="text-align: right">Measurement</p></td>
   <td>A field that implies the type of measurement being performed. Each measurement is exclusive to a particular physical quantity (e.g., temperature), but which may have multiple valid units of measurement (C, F, K). This subfield is required for any numeric field with a point type other than `count`.
   </td>
   <td>Temperature, flowrate, pressure</td>
   <td>1</td>
   <td>Optional</td>
  </tr>
  <tr>
   <td><p style="text-align: right">Point Type</p></td>
   <td>Defines the function of the point across several layers of context: directionality (input/output), reading type (analog, input, multistate), telemetric versus static data (label and capacity being static; sensor and setpoint being active), etc. This is the one component that is required for every field.
   </td>
   <td>Sensor, Setpoint, Status, Command, Count, Accumulator</td>
   <td>1</td>
   <td>Required</td>
  </tr>
</table>

**Note:** See [Process Automation model](model_process_automation.md) for details on operating limits.

### Fields

Fields are constructed by combining subfields in a structured way to define very specific semantic concepts. Field names are intended to read