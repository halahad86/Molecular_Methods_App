from django.core.management.base import BaseCommand

import app.models


class Command(BaseCommand):

    args = 'No arguments'

    help = 'Populate lab table of database'

    def handle(self, *args, **options):

        app.models.Lab.objects.get_or_create(
            name="PCR",
            number=1,
            ILO="<ul><li>Describe the theory of, and be able to design and perform, a polymerase chain reaction (PCR) reaction</li><li>Understand the principles behind PCR primer design</li><li>Analyse PCR results from gel electrophoresis</li></ul>",
            tasks="<ul><li>Set up PCR</li><li>Run PCR</li><li>Perform gel electrophoresis with PCR samples</li><li>Purify the PCR sample</li><li>Analyse results from gel electrophoresis</li><li>Undertake Exercise 'PCR and Primer Design'</li><li>Undertake Computing Exercise 'Designing a PCR Experiment'</li></ul>")[0]

        app.models.Lab.objects.get_or_create(
            name="Ligation and transformation",
            number=2,
            ILO="<ul><li>Describe the strategies used in cloning DNA into a suitable plasmid vector</li><li>Describe, and be able to perform, transformation of E.coli with a plasmid</li><li>Be able to perform calculations relating to Molecular Methods, including transformation efficiency, dilutions and concentrations</li></ul>",
            tasks="<ul><li>Restriction digest PCR sample</li><li>Ligate PCR product into a digested plasmid vector</li><li>Transform E.coli with recombinant plasmid</li><li>Undertake Exercise 'Calculations'</li></ul>")[0]

        app.models.Lab.objects.get_or_create(
            name="Blue/White Screening",
            number=3,
            ILO="<ul><li>Explain the principles and purpose of antibiotic selection and blue/white screening</li><li>Understand your agar plates and class controls</li></ul>",
            tasks="<ul><li>Analyse agar plates, including all controls</li><li>Grow blue and white E.coli colonies in liquid culture overnight</li></ul>")[0]

        app.models.Lab.objects.get_or_create(
            name="Plasmid Miniprep",
            number=4,
            ILO="<ul><li>Describe and perform a small-scale plasmid purification from an overnight culture</li><li>Understand the concept of, and be able to deduce, a restriction map for a plasmid</li></ul>",
            tasks="<ul><li>Harvest and mini-prep E. coli cultures in order to purify plasmids</li><li>Check the success of the cloning procedure by restriction digest and gel electrophoresis</li><li>Undertake Exercise 'Restriction Mapping'</li></ul>")[0]

        app.models.Lab.objects.get_or_create(
            name="DNA sequencing",
            number=5,
            ILO="<ul><li>Understand the principle of dideoxy sequencing of a plasmid</li><li>Compare and contrast the theoretical principles of manual and automated sequencing</li><li>Be able to perform and understand DNA sequence analyses</li></ul>",
            tasks="<ul><li>Complete the 'Sequencing' section of the lab</li><li>Examine and analyse DNA sequence data from the fragment of DNA you have cloned in Computer Exercise 'Sequence Analysis'</li></ul>")[0]

        app.models.Lab.objects.get_or_create(
            name="Real-time quantitative PCR",
            number=6,
            ILO="<ul><li>Describe the theory of, and be able to design and perform, a real-time quantitative polymerase chain reaction (PCR) reaction</li><li>Understand the different applications of conventional PCR vs RT-qPCR</li><li>Compare and contrast PCR and real-time qPCR</li><li>Analyse real-time qPCR data</li></ul>",
            tasks="<ul><li>Design primers to amplify the HIV gene sequence</li><li>Set up RT-qPCR and conventional PCR</li><li>Perform gel electrophoresis of conventional PCR</li><li>Analyse RT-qPCR data in Computing Exercise 'Real-time qPCR Data Analysis'</li></ul>")[0]
