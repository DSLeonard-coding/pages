Copyright Douglas S. Leonard 2024.  All rights reserved
Licenses are shown in each link.  If in doubt, all rights, reserved/ask, especially for **for the non-public repos, where license text is a draft only.**  Generally, I don't like gpl, particularly gpl3.


## Notebooks and wikis:

---

- [Properties and C# vs python, Jupyter notebook](Csharp_vs_python_jupyter.html)
- [Setting up an SoS multi-language Jupyter Notebook](SoS-install.html)
- [Multi-language list benchmark tests](benchmarks.html)
- [My wiki about how to unerstand git](https://gitlab.com/douglas.s.leonard/gitwiki)


## Public Physics utilities/libraries:

---
- **[DLG4::VolumeBuilders: A documented, streamlined, fluent geometry API for Geant4](https://douglas_s_leonard.gitlab.io/physics_utilities/VolumeBuilders/)**
- [alldat: Data read/write/conversion and utility clas for Ortec and root formats](https://gitlab.com/douglas.s.leonard/alldat)
- [UAO2_PLTLY: Representative use of PLTLY.NET for interactive plots ]( https://gitlab.com/douglas.s.leonard/UAO2_PLTLY)

## Misc utilities:

---

### **git**
- [git-alltrees subtree behavior with root-tree compliment and seamless merge history (no-squash/duplicates)](https://gitlab.com/douglas.s.leonard/alltrees/-/wikis/home)

### **python:** (mostly packaged for pip use)
- [qx: Console command/log-level convenience utility for phython](https://gitlab.com/douglas.s.leonard/qx)  This one is pretty handy for CLI scripting.
- [strictdataclasses: Prevents many un-intentional or ad-hoc modification of dataclasses](https://gitlab.com/douglas.s.leonard/strictdataclasses) Now with extensive test/demonstration/CI/CD


### **C-sharp/C#** (my favorite language):
- [UAO2_PLTLY: Representative use of PLTLY.NET for interactive plots ]( https://gitlab.com/douglas.s.leonard/UAO2_PLTLY)
- [[Fitfix:  Fixes garmin fit files with corrupt times](https://gitlab.com/douglas.s.leonard/FitFix)  alpha code, but it works. My first C# project.

### C++
- [ Heterogeneous tuple order/sort by column priority list](https://gitlab.com/douglas_s_leonard/programming_utilities/cpp/tuple_comp)  Good for sorting column-wise heterogeneous output. Harder than it sounds.

### Other
- [DOCTocActions:  A simple auto Table of Contents generator script for markdown on github repos](https://github.com/marketplace/actions/doctoc-action) Just the sctript is mine, not the genertor.


## Internal physics tools (access may be required):
- [DecayChain: WIP, A decay network buider/analyzer parsing endsf data files](https://gitlab.com/douglas_s_leonard/physics_utilities/DecayChain)  This may go public.
- [HpgeSim:  CupSIM/GLG4SIM/ect based HPGe Geant sim with a focus on flexible sample/source batch deployment and portability](https://gitlab.com/douglas.s.leonard/HpgeSim)
- [HpgeSim-distrib:  Same as above but without proprietary models, may not be as updated](https://gitlab.com/douglas.s.leonard/HpgeSim)
- [HpgeAnalys:  Data processing pipeline/event-/histogram-builder for CUP HPGe data and sims](https://gitlab.com/douglas.s.leonard/HpgeSim)  Shares event selection and usage interface for Sim/Data.
- [gdcodes/gdfit: Branching/Intensity-constrained multi-activity peak fitting targetting HPGe](https://gitlab.com/douglas.s.leonard/gdcodes) This code has a lot of history.  It shows, but it works. Used originally for NAA analysis in EXO, although that was an adaptation too. Uses alldat for data reading.  Now includes a python API for automation.

## Comming soon:

---

- A cookie cutter for easy creation and straight-to-git(lab/hub) deployment of new pip-installable python projects, so you can just code.
- A vscode extension to report and export an organized view of extensions and packs per profile.
- DecayChain may go public.

## How this page was made:

---

This is a gitlab-pages page.  The underlying repo is here: [Link](https://gitlab.com/douglas_s_leonard/pages).
I just use scripts to generate static html in public/  and the only thing needed to publish on gitlab is the .gitlab-ci.yml and enabling pages in the project.

