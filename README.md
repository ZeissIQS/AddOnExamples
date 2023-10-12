# AddOnExamples

This repository contains various [ZEISS INSPECT](https://www.zeiss.com/metrology/products/software.html#inspectionsolutions) Add-on examples for educational and inspirational purposes.

> [!NOTE]
> Please have a look into the [ZEISS INSPECT add-on documentation](https://zeissiqs.github.io/) for a general introduction to ZEISS INSPECT Add-on development, a set of documented Add-on examples and the API specification.

In principle, a ZEISS INSPECT Add-on is just a zip'ed directory with a special structure, containing script, templates, definitions etc. necessary to add features to the ZEISS Inspect software. The Add-ons listed here can be downloaded in compressed form via the ZEISS Quality Software Store in the [ZEISS Quality Suite](https://www.zeiss.com/metrology/products/software.html). Alternatively, for fiddling around with them, the Add-ons repository can, too, be cloned, zip'ed and then dropped right into ZEISS Inspect. Please see the documentation mentioned above for more details or consult the [training center](https://training.gom.com) for a general feature overview.

## Complete add-on examples

* Measurement System Analysis Add-on: [MSA](examples/MeasurementSystemAnalysis)

## Add-on programming examples

* Access resources from within scripts: [ResourceAccess](examples/ResourceAccess)
* Display measurement data from a scan as an image in a user-defined dialog: [DisplayImage](examples/DisplayImage)
* Extract text from images (measurement data) and provide it as a scripted actual element: [TextDetection](examples/TextDetection)
* Save settings persistently using the `settings` API: [SettingsAPI](examples/SettingsAPI)
