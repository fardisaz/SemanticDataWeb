# -*- coding: utf-8 -*-
from rdflib import Graph, Literal, BNode, Namespace, RDF, URIRef
from rdflib.namespace import DC, FOAF
from rdflib import Namespace



n = Namespace("http://example.org/")
g = Graph()

# Create an identifier to use as the subject for Donna.
Order1 = BNode()



s1 = []


UNH = []
UNHElements = 0
UNHComponents = []

BGM=[]
BGMElements=0
BGMComponents=[]

DTM = []
DTMElements = 0
DTMComponents = []

NAD = []
NADElements = 0
NADComponents = []

LIN = []
LINElements = 0
LINComponents = []

QTY = []
QTYElements = 0
QTYComponents = []

PRI = []
PRIElements = 0
PRIComponents = []

UNS = []
UNSElements = 0

CNT = []
CNTElements = 0
CNTComponents = []

UNT=[]
UNTElements = 0

PAI = []
PAIElements = 0
PAIComponents = []

ALI = []
ALIElements = 0

IMD = []
IMDElements = 0
IMDComponents = []

FTX = []
FTXElements = 0
FTXComponents = []

GIR = []
GIRElements = 0
GIRComponents = []

RFF = []
RFFElements = 0
RFFComponents = []

LOC = []
LOCElements = 0
LOCComponents = []

FII = []
FIIElements = 0
FIIComponents = []

PCD = []
PCDElements = 0
PCDComponents = []

MOA = []
MOAElements = 0
MOAComponents = []

RTE = []
RTEElements = 0
RTEComponents = []

TAX = []
TAXElements = 0
TAXComponents = []

RCS = []
RCSElements = 0
RCSComponents = []

DGS = []
DGSElements = 0
DGSComponents = []

CTA = []
CTAElements = 0
CTAComponents = []

COM = []
COMElements = 0
COMComponents = []

PIA= []
PIAElements = 0
PIAComponents = []

GEI = []
GEIElements = 0
GEIComponents = []

GIN = []
GINElements = 0
GINComponents = []

QVR = []
QVRElements = 0
QVRComponents = []

DOC = []
DOCElements = 0
DOCComponents = []

MTD = []
MTDElements = 0
MTDComponents = []

CCI = []
CCIElements = 0
CCIComponents = []

CAV = []
CAVElements = 0
CAVComponents = []

PCI = []
PCIElements = 0
PCIComponents = []

CUX = []
CUXElements = 0
CUXComponents = []

PYT = []
PYTElements = 0
PYTComponents = []

RJL = []
RJLElements = 0
RJLComponents = []

TDT = []
TDTElements = 0
TDTComponents = []

TOD = []
TODElements = 0
TODComponents = []

PAC = []
PACElements = 0
PACComponents  = []

MEA = []
MEAElements = 0
MEAComponents = []

EQD = []
EQDElements = 0
EQDComponents = []

HAN = []
HANElements = 0
HANComponents = []

SCC = []
SCCElements = 0
SCCComponents = []

APR = []
APRElements = 0
APRComponents = []

RNG = []
RNGElements = 0
RNGComponents = []

ALC = []
ALCElements = 0
ALCComponents = []

STG = []
STGElements = 0
STGComponents = []

EFI = []
EFIElements = 0
EFIComponents = []

CED = []
CEDElements = 0
CEDComponents = []

STS = []
STSElements = 0
STSComponents = []

l = []

with open("order1.txt") as fh:
    for line in fh:
        if line.startswith("UNH"):
            l = line.split("’")[0]
            s1 = l.split('+')
            UNHElements = len(s1)
            for i in range(len(s1)):
                UNH.append(s1[i].split(':'))
                UNHComponents.append(len(s1[i].split(':')))
                
        if line.startswith("ALC"):
            l = line.split("’")[0]
            s1 = l.split('+')
            ALCElements = len(s1)
            ALC = []
            ALCComponents = []
            for i in range(len(s1)):
                ALC.append(s1[i].split(':'))
                ALCComponents.append(len(s1[i].split(':')))
                
        if line.startswith("RNG"):
            l = line.split("’")[0]
            s1 = l.split('+')
            RNGElements = len(s1)
            RNG = []
            RNGComponents = []
            for i in range(len(s1)):
                RNG.append(s1[i].split(':'))
                RNGComponents.append(len(s1[i].split(':')))
                
        if line.startswith("APR"):
            l = line.split("’")[0]
            s1 = l.split('+')
            APRElements = len(s1)
            APR = []
            APRComponents = []
            for i in range(len(s1)):
                APR.append(s1[i].split(':'))
                APRComponents.append(len(s1[i].split(':')))
                
        if line.startswith("SCC"):
            l = line.split("’")[0]
            s1 = l.split('+')
            SCCElements = len(s1)
            SCC = []
            SCCComponents = []
            for i in range(len(s1)):
                SCC.append(s1[i].split(':'))
                SCCComponents.append(len(s1[i].split(':')))
                
        if line.startswith("HAN"):
            l = line.split("’")[0]
            s1 = l.split('+')
            HANElements = len(s1)
            HAN = []
            HANComponents = []
            for i in range(len(s1)):
                HAN.append(s1[i].split(':'))
                HANComponents.append(len(s1[i].split(':')))
                
        if line.startswith("EQD"):
            l = line.split("’")[0]
            s1 = l.split('+')
            EQDElements = len(s1)
            EQD = []
            EQDComponents = []
            for i in range(len(s1)):
                EQD.append(s1[i].split(':'))
                EQDComponents.append(len(s1[i].split(':')))
        
        if line.startswith("MEA"):
            l = line.split("’")[0]
            s1 = l.split('+')
            MEAElements = len(s1)
            MEA = []
            MEAComponents = []
            for i in range(len(s1)):
                MEA.append(s1[i].split(':'))
                MEAComponents.append(len(s1[i].split(':')))
                
        if line.startswith("PAC"):
            l = line.split("’")[0]
            s1 = l.split('+')
            PACElements = len(s1)
            PAC = []
            PACComponents = []
            for i in range(len(s1)):
                PAC.append(s1[i].split(':'))
                PACComponents.append(len(s1[i].split(':')))
                
        if line.startswith("TOD"):
            l = line.split("’")[0]
            s1 = l.split('+')
            TODElements = len(s1)
            TOD = []
            TODComponents = []
            for i in range(len(s1)):
                TOD.append(s1[i].split(':'))
                TODComponents.append(len(s1[i].split(':')))
                
        if line.startswith("TDT"):
            l = line.split("’")[0]
            s1 = l.split('+')
            TDTElements = len(s1)
            TDT = []
            TDTComponents = []
            for i in range(len(s1)):
                TDT.append(s1[i].split(':'))
                TDTComponents.append(len(s1[i].split(':')))
                
        if line.startswith("RJL"):
            l = line.split("’")[0]
            s1 = l.split('+')
            RJLElements = len(s1)
            RJL = []
            RJLComponents = []
            for i in range(len(s1)):
                RJL.append(s1[i].split(':'))
                RJLComponents.append(len(s1[i].split(':')))
        
        if line.startswith("PYT"):
            l = line.split("’")[0]
            s1 = l.split('+')
            PYTElements = len(s1)
            PYT = []
            PYTComponents = []
            for i in range(len(s1)):
                PYT.append(s1[i].split(':'))
                PYTComponents.append(len(s1[i].split(':')))
        
        if line.startswith("CUX"):
            l = line.split("’")[0]
            s1 = l.split('+')
            CUXElements = len(s1)
            CUX = []
            CUXComponents = []
            for i in range(len(s1)):
                CUX.append(s1[i].split(':'))
                CUXComponents.append(len(s1[i].split(':')))
                
        if line.startswith("FII"):
            l = line.split("’")[0]
            s1 = l.split('+')
            FIIElements = len(s1)
            FII = []
            FIIComponents = []
            for i in range(len(s1)):
                FII.append(s1[i].split(':'))
                FIIComponents.append(len(s1[i].split(':')))
                
        if line.startswith("LOC"):
            l = line.split("’")[0]
            s1 = l.split('+')
            LOCElements = len(s1)
            LOC = []
            LOCComponents = []
            for i in range(len(s1)):
                LOC.append(s1[i].split(':'))
                LOCComponents.append(len(s1[i].split(':')))
                
        if line.startswith("BGM"):
            l = line.split("’")[0]
            s1 = l.split('+')
            BGMElements=len(s1)
            for i in range(len(s1)):
                BGM.append(s1[i].split(':'))
                BGMComponents.append(len(s1[i].split(':')))  

        if line.startswith("DTM"):
            l = line.split("’")[0]
            s1 = l.split('+')
            DTMElements = len(s1)
            DTM = []
            DTMComponents = []
            for i in range(len(s1)):
                DTM.append(s1[i].split(':'))
                DTMComponents.append(len(s1[i].split(':')))

        if line.startswith("NAD"):
            l = line.split("’")[0]
            s1 = l.split('+')
            NADElements = len(s1)
            NAD = []
            NADComponents = []
            for i in range(len(s1)):
                NAD.append(s1[i].split(':'))
                NADComponents.append(len(s1[i].split(':')))

        if line.startswith("LIN"):
            l = line.split("’")[0]
            s1 = l.split('+')
            LINElements = len(s1)
            LIN = []
            LINComponents = []
            for i in range(len(s1)):
                LIN.append(s1[i].split(':'))
                LINComponents.append(len(s1[i].split(':')))

        if line.startswith("QTY"):
            l = line.split("’")[0]
            s1 = l.split('+')
            QTYElements = len(s1)
            QTY = []
            QTYComponents = []
            for i in range(len(s1)):
                QTY.append(s1[i].split(':'))
                QTYComponents.append(len(s1[i].split(':')))

        if line.startswith("PRI"):
            l = line.split("’")[0]
            s1 = l.split('+')
            PRIElements = len(s1)
            PRI = []
            PRIComponents = []
            for i in range(len(s1)):
                PRI.append(s1[i].split(':'))
                PRIComponents.append(len(s1[i].split(':')))
                
        if line.startswith("IMD"):
            l = line.split("’")[0]
            s1 = l.split('+')
            IMDElements = len(s1)
            IMD = []
            IMDComponents  = []
            for i in range(len(s1)):
                IMD.append(s1[i].split(':'))
                IMDComponents.append(len(s1[i].split(':')))
        
        if line.startswith("UNS"):
            l = line.split("’")[0]
            s1 = l.split('+')
            UNSElements = len(s1)
            for i in range(len(s1)):
                UNS.append(s1[i].split(':'))
            
        if line.startswith("ALI"):
            l = line.split("’")[0]
            s1 = l.split('+')
            ALIElements = len(s1)
            ALI = []
            ALIComponents = []
            for i in range(len(s1)):
                ALI.append(s1[i].split(':'))
                ALIComponents.append(len(s1[i].split(':')))

        if line.startswith("CNT"):
            l = line.split("’")[0]
            s1 = l.split('+')
            CNTElements = len(s1)
            CNT = []
            CNTComponents = []
            for i in range(len(s1)):
                CNT.append(s1[i].split(':'))
                CNTComponents.append(len(s1[i].split(':')))
        
        if line.startswith("RFF"):
            l = line.split("’")[0]
            s1 = l.split('+')
            RFFElements = len(s1)
            RFF = []
            RFFComponents = []
            for i in range(len(s1)):
                RFF.append(s1[i].split(':'))
                RFFComponents.append(len(s1[i].split(':')))
                
        if line.startswith("PAI"):
            l = line.split("’")[0]
            s1 = l.split('+')
            PAIElements = len(s1)
            PAI = []
            PAIComponents = []
            for i in range(len(s1)):
                PAI.append(s1[i].split(':'))
                PAIComponents.append(len(s1[i].split(':')))
                
        if line.startswith("GIR"):
            l = line.split("’")[0]
            s1 = l.split('+')
            GIRElements = len(s1)
            GIR = []
            GIRComponents = []
            for i in range(len(s1)):
                GIR.append(s1[i].split(':'))
                GIRComponents.append(len(s1[i].split(':')))
                
        if line.startswith("FTX"):
            l = line.split("’")[0]
            s1 = l.split('+')
            FTXElements = len(s1)
            FTX = []
            FTXComponents = []
            for i in range(len(s1)):
                FTX.append(s1[i].split(':'))
                FTXComponents.append(len(s1[i].split(':')))

        if line.startswith("UNT"):
            l = line.split("’")[0]
            s1 = l.split('+')
            UNTElements = len(s1)
            for i in range(len(s1)):
                UNT.append(s1[i])

        if line.startswith("PCD"):
            l = line.split("’")[0]
            s1 = l.split('+')
            PCDElements = len(s1)
            PCD = []
            PCDComponents = []
            for i in range(len(s1)):
                PCD.append(s1[i].split(':'))
                PCDComponents.append(len(s1[i].split(':')))

        if line.startswith("MOA"):
            l = line.split("’")[0]
            s1 = l.split('+')
            MOAElements = len(s1)
            MOA = []
            MOAComponents = []
            for i in range(len(s1)):
                MOA.append(s1[i].split(':'))
                MOAComponents.append(len(s1[i].split(':')))

        if line.startswith("RTE"):
            l = line.split("’")[0]
            s1 = l.split('+')
            RTEElements = len(s1)
            RTE = []
            RTEComponents = []
            for i in range(len(s1)):
                RTE.append(s1[i].split(':'))
                RTEComponents.append(len(s1[i].split(':')))

        if line.startswith("TAX"):
            l = line.split("’")[0]
            s1 = l.split('+')
            TAXElements = len(s1)
            TAX = []
            TAXComponents = []
            for i in range(len(s1)):
                TAX.append(s1[i].split(':'))
                TAXComponents.append(len(s1[i].split(':')))

        if line.startswith("RCS"):
            l = line.split("’")[0]
            s1 = l.split('+')
            RCSElements = len(s1)
            RCS = []
            RCSComponents = []
            for i in range(len(s1)):
                RCS.append(s1[i].split(':'))
                RCSComponents.append(len(s1[i].split(':')))

        if line.startswith("DGS"):
            l = line.split("’")[0]
            s1 = l.split('+')
            DGSElements = len(s1)
            DGS = []
            DGSComponents = []
            for i in range(len(s1)):
                DGS.append(s1[i].split(':'))
                DGSComponents.append(len(s1[i].split(':')))

        if line.startswith("CTA"):
            l = line.split("’")[0]
            s1 = l.split('+')
            CTAElements = len(s1)
            CTA = []
            CTAComponents = []
            for i in range(len(s1)):
                CTA.append(s1[i].split(':'))
                CTAComponents.append(len(s1[i].split(':')))

        if line.startswith("COM"):
            l = line.split("’")[0]
            s1 = l.split('+')
            COMElements = len(s1)
            COM = []
            COMComponents = []
            for i in range(len(s1)):
                COM.append(s1[i].split(':'))
                COMComponents.append(len(s1[i].split(':')))

        if line.startswith("PIA"):
            l = line.split("’")[0]
            s1 = l.split('+')
            PIAElements = len(s1)
            PIA = []
            PIAComponents = []
            for i in range(len(s1)):
                PIA.append(s1[i].split(':'))
                PIAComponents.append(len(s1[i].split(':')))

        if line.startswith("GEI"):
            l = line.split("’")[0]
            s1 = l.split('+')
            GEIElements = len(s1)
            GEI = []
            GEIComponents = []
            for i in range(len(s1)):
                GEI.append(s1[i].split(':'))
                GEIComponents.append(len(s1[i].split(':')))

        if line.startswith("GIN"):
            l = line.split("’")[0]
            s1 = l.split('+')
            GINElements = len(s1)
            GIN = []
            GINComponents = []
            for i in range(len(s1)):
                GIN.append(s1[i].split(':'))
                GINComponents.append(len(s1[i].split(':')))

        if line.startswith("QVR"):
            l = line.split("’")[0]
            s1 = l.split('+')
            QVRElements = len(s1)
            QVR = []
            QVRComponents = []
            for i in range(len(s1)):
                QVR.append(s1[i].split(':'))
                QVRComponents.append(len(s1[i].split(':')))

        if line.startswith("DOC"):
            l = line.split("’")[0]
            s1 = l.split('+')
            DOCElements = len(s1)
            DOC = []
            DOCComponents = []
            for i in range(len(s1)):
                DOC.append(s1[i].split(':'))
                DOCComponents.append(len(s1[i].split(':')))

        if line.startswith("MTD"):
            l = line.split("’")[0]
            s1 = l.split('+')
            MTDElements = len(s1)
            MTD = []
            MTDComponents = []
            for i in range(len(s1)):
                MTD.append(s1[i].split(':'))
                MTDComponents.append(len(s1[i].split(':')))

        if line.startswith("CCI"):
            l = line.split("’")[0]
            s1 = l.split('+')
            CCIElements = len(s1)
            CCI = []
            CCIComponents = []
            for i in range(len(s1)):
                CCI.append(s1[i].split(':'))
                CCIComponents.append(len(s1[i].split(':')))

        if line.startswith("CAV"):
            l = line.split("’")[0]
            s1 = l.split('+')
            CAVElements = len(s1)
            CAV = []
            CAVComponents = []
            for i in range(len(s1)):
                CAV.append(s1[i].split(':'))
                CAVComponents.append(len(s1[i].split(':')))

        if line.startswith("PCI"):
            l = line.split("’")[0]
            s1 = l.split('+')
            PCIElements = len(s1)
            PCI = []
            PCIComponents = []
            for i in range(len(s1)):
                PCI.append(s1[i].split(':'))
                PCIComponents.append(len(s1[i].split(':')))

        if line.startswith("STG"):
            l = line.split("’")[0]
            s1 = l.split('+')
            STGElements = len(s1)
            STG = []
            STGComponents = []
            for i in range(len(s1)):
                STG.append(s1[i].split(':'))
                STGComponents.append(len(s1[i].split(':')))

        if line.startswith("EFI"):
            l = line.split("’")[0]
            s1 = l.split('+')
            EFIElements = len(s1)
            EFI = []
            EFIComponents = []
            for i in range(len(s1)):
                EFI.append(s1[i].split(':'))
                EFIComponents.append(len(s1[i].split(':')))

        if line.startswith("CED"):
            l = line.split("’")[0]
            s1 = l.split('+')
            CEDElements = len(s1)
            CED = []
            CEDComponents = []
            for i in range(len(s1)):
                CED.append(s1[i].split(':'))
                CEDComponents.append(len(s1[i].split(':')))

        if line.startswith("STS"):
            l = line.split("’")[0]
            s1 = l.split('+')
            STSElements = len(s1)
            STS = []
            STSComponents = []
            for i in range(len(s1)):
                STS.append(s1[i].split(':'))
                STSComponents.append(len(s1[i].split(':')))



        #UNH

        g.add((Order1, n.MessageReferenceNumber, Literal(UNH[1][0])))

        if UNHElements >= 3:
            g.add((Order1, n.MessageType, Literal(UNH[2][0])))
            if UNHComponents[2] >= 2:
                g.add((Order1, n.MessageVersionNumber, Literal(UNH[2][1])))
                if UNHComponents[2] >= 3:
                    g.add((Order1, n.MessageReleaseNumber, Literal(UNH[2][2])))
                    if UNHComponents[2] >= 4:
                        g.add((Order1, n.ControllingAgencyCoded, Literal(UNH[2][3])))
                        if UNHComponents[2] >= 5:
                            g.add((Order1, n.AssociationAssignedCode, Literal(UNH[2][4])))
                            if UNHComponents[2] >= 6:
                                g.add((Order1, n.CodeListDirectoryVersionNumber, Literal(UNH[2][5])))
                                if UNHComponents[2] >= 7:
                                    g.add((Order1, n.MessageTypeSubFunctionIdentification, Literal(UNH[2][6])))
        if UNHElements >= 4:
            g.add((Order1, n.CommonAccessReference, Literal(UNH[3][0])))
        if UNHElements >= 5:
            g.add((Order1, n.SequenceOfTransfers, Literal(UNH[4][0])))
            if UNHComponents[4] >= 2:
                g.add((Order1, n.FirstAndLastTransfer, Literal(UNH[4][1])))
        if UNHElements >= 6:
            g.add((Order1, n.MessageSubsetIdentification, Literal(UNH[5][0])))
            if UNHComponents[5] >= 2:
                g.add((Order1, n.MessageSubsetVersionNumber, Literal(UNH[5][1])))
                if UNHComponents[5] >= 3:
                    g.add((Order1, n.MessageSubsetReleaseNumber, Literal(UNH[5][2])))
                    if UNHComponents[5] >= 4:
                        g.add((Order1, n.ControllingAgencyCoded, Literal(UNH[5][3])))
        if UNHElements >= 7:
            g.add((Order1, n.MessageImplementationGuidelineIdentification, Literal(UNH[6][0])))
            if UNHComponents[6] >= 2:
                g.add((Order1, n.MessageImplementationGuidelineVersionNumber, Literal(UNH[6][1])))
                if UNHComponents[6] >= 3:
                    g.add((Order1, n.MessageImplementationGuidelineReleaseNumber, Literal(UNH[6][2])))
                    if UNHComponents[6] >= 4:
                        g.add((Order1, n.ControllingAgencyCoded, Literal(UNH[6][3])))
        if UNHElements >= 8:
            g.add((Order1, n.ScenarioIdentification, Literal(UNH[7][0])))
            if UNHComponents[7] >= 2:
                g.add((Order1, n.ScenarioVersionNumber, Literal(UNH[7][1])))
                if UNHComponents[7] >= 3:
                    g.add((Order1, n.ScenarioReleaseNumber, Literal(UNH[7][2])))
                    if UNHComponents[7] >= 4:
                        g.add((Order1, n.ControllingAgencyCoded, Literal(UNH[7][3])))

        #IMD
        if IMDElements >= 2:
            g.add((Order1, n.DescriptionFormatCode, Literal(IMD[1][0])))
        if IMDElements >= 3:
            if IMDComponents[2] >= 1:
                g.add((Order1, n.ItemCharacteristicCode, Literal(IMD[2][0])))
                if IMDComponents[2] >= 2:
                    g.add((Order1, n.CodeListIdentificationCode, Literal(IMD[2][1])))
                    if IMDComponents[2] >= 3:
                        g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(IMD[2][2])))
        if IMDElements >= 4:
            if IMDComponents[3] >= 1:
                g.add((Order1, n.ItemDescriptionCode, Literal(IMD[3][0])))
                if IMDComponents[3] >= 2:
                    g.add((Order1, n.CodeListIdentificationCode, Literal(IMD[3][1])))
                    if IMDComponents[3] >= 3:
                        g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(IMD[3][2])))
                        if IMDComponents[3] >= 4:
                            g.add((Order1, n.ItemDescription, Literal(IMD[3][3])))
                            if IMDComponents[3] >= 5:
                                g.add((Order1, n.ItemDescription, Literal(IMD[3][4])))
                                if IMDComponents[3] >= 6:
                                    g.add((Order1, n.LanguageNameCode, Literal(IMD[3][5])))
        if IMDElements >= 5:
            g.add((Order1, n.SufaceOrLayerCode, Literal(IMD[4][0])))

        #ALC
        if ALCElements >= 2:
            g.add((Order1, n.AllowanceOrChargeCodeQualifier, Literal(ALC[1][0])))
        if ALCElements >= 3:
            if ALCComponents[2] >= 1:
                g.add((Order1, n.AllowanceOrChargeIdentifier, Literal(ALC[2][0])))
                if ALCComponents[2] >= 2:
                    g.add((Order1, n.AllowanceOrChargeIdentificationCode, Literal(ALC[2][1])))
        if ALCElements >= 4:
            g.add((Order1, n.SettlementMeansCode, Literal(ALC[3][0])))
        if ALCElements >= 5:
            g.add((Order1, n.CalculationSequenceCode, Literal(ALC[4][0])))
        if ALCElements >= 6:
            if ALCComponents[5] >= 1:
                g.add((Order1, n.SpecialServiceDescriptionCode, Literal(ALC[5][0])))
                if ALCComponents[5] >= 2:
                    g.add((Order1, n.CodeListIdentificationCode, Literal(ALC[5][1])))
                    if ALCComponents[5] >= 3:
                        g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(ALC[5][2])))
                        if ALCComponents[5] >= 4:
                            g.add((Order1, n.SpecialServiceDescription, Literal(ALC[5][3])))
                            if ALCComponents[5] >= 5:
                                g.add((Order1, n.SpecialServiceDescription, Literal(ALC[5][4])))


        #RNG
        if RNGElements >= 2:
            g.add((Order1, n.RangeTypeCodeQualifier, Literal(RNG[1][0])))
        if RNGElements >= 3:
            if RNGComponents[2] >= 1:
                g.add((Order1, n.MeasurementUnitCode, Literal(RNG[2][0])))
                if RNGComponents[2] >= 2:
                    g.add((Order1, n.RangeMinimumQuantity, Literal(RNG[2][1])))
                    if RNGComponents[2] >= 3:
                        g.add((Order1, n.RangeMaximumQuantity, Literal(RNG[2][2])))


        #SCC
        if SCCElements >= 2:
            g.add((Order1, n.DeliveryPlanCommitmentLevelCode, Literal(SCC[1][0])))
        if SCCElements >= 3:
            g.add((Order1, n.DeliveryInstructionCode, Literal(SCC[2][0])))
        if SCCElements >= 4:
            if SCCComponents[3] >= 1:
                g.add((Order1, n.FrequencyCode, Literal(SCC[3][0])))
                if SCCComponents[3] >= 2:
                    g.add((Order1, n.DespatchPatternCode, Literal(SCC[3][1])))
                    if SCCComponents[3] >= 3:
                        g.add((Order1, n.DespatchPatternTimingCode, Literal(SCC[3][2])))

        #APR
        if APRElements >= 2:
            g.add((Order1, n.TradeClassCode, Literal(APR[1][0])))
        if APRElements >= 3:
            if APRComponents[2] >= 1:
                g.add((Order1, n.PriceMultiplierRate, Literal(APR[2][0])))
                if APRComponents[2] >= 2:
                    g.add((Order1, n.PriceMultiplierTypeCodeQualifier, Literal(APR[2][1])))
        if APRElements >= 4:
            if APRComponents[3] >= 1:
                g.add((Order1, n.ChangeReasonDescriptionCode, Literal(APR[3][0])))
                if APRComponents[3] >= 2:
                    g.add((Order1, n.CodeListIdentificationCode, Literal(APR[3][1])))
                    if APRComponents[3] >= 3:
                        g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(APR[3][2])))
                        if APRComponents[3] >= 4:
                            g.add((Order1, n.ChangeReasonDescription, Literal(APR[3][3])))


        #HAN
        if HANElements >= 2:
            if HANComponents[1] >= 1:
                g.add((Order1, n.HandlingInstructionDescriptionCode, Literal(HAN[1][0])))
                if HANComponents[1] >= 2:
                    g.add((Order1, n.CodeListIdentificationCode, Literal(HAN[1][1])))
                    if HANComponents[1] >= 3:
                        g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(HAN[1][2])))
                        if HANComponents[1] >= 4:
                            g.add((Order1, n.HandlingInstructionDescription, Literal(HAN[1][3])))
        if HANElements >= 3:
            if HANComponents[2] >= 1:
                g.add((Order1, n.HazardousMaterialCategoryNameCode, Literal(HAN[2][0])))
                if HANComponents[2] >= 2:
                    g.add((Order1, n.CodeListIdentificationCode, Literal(HAN[2][1])))
                    if HANComponents[2] >= 3:
                        g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(HAN[2][2])))
                        if HANComponents[2] >= 4:
                            g.add((Order1, n.HazardousMaterialCategoryName, Literal(HAN[2][3])))


        #TDT
        if TDTElements >= 2:
            g.add((Order1, n.TransportStageCodeQualifier, Literal(TDT[1][0])))
        if TDTElements >= 3:
            g.add((Order1, n.MeansOfTransportJourneyIdentifier, Literal(TDT[2][0])))
        if TDTElements >= 4:
            if TDTComponents[3] >= 1:
                g.add((Order1, n.TransportModeNameCode, Literal(TDT[3][0])))
                if TDTComponents[3] >= 2:
                    g.add((Order1, n.TransportModeName, Literal(TDT[3][1])))
        if TDTElements >= 5:
            if TDTComponents[4] >= 1:
                g.add((Order1, n.TransportMeansDescriptionCode, Literal(TDT[4][0])))
                if TDTComponents[4] >= 2:
                    g.add((Order1, n.CodeListIdentificationCode, Literal(TDT[4][1])))
                    if TDTComponents[4] >= 3:
                        g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(TDT[4][2])))
                        if TDTComponents[4] >= 4:
                            g.add((Order1, n.TransportMeansDescription, Literal(TDT[4][3])))
        if TDTElements >= 6:
            if TDTComponents[5] >= 1:
                g.add((Order1, n.CarrierIdentification, Literal(TDT[5][0])))
                if TDTComponents[5] >= 2:
                    g.add((Order1, n.CodeListIdentificationCode, Literal(TDT[5][1])))
                    if TDTComponents[5] >= 3:
                        g.add((Order1, n.CodeListResponsibleAgencyCoded, Literal(TDT[5][2])))
                        if TDTComponents[5] >= 4:
                            g.add((Order1, n.CarrierName, Literal(TDT[5][3])))
        if TDTElements >= 7:
            g.add((Order1, n.TransitDirectionIndicatorCode, Literal(TDT[6][0])))
        if TDTElements >= 8:
            if TDTComponents[7] >= 1:
                g.add((Order1, n.ExcessTransportationReasonCode, Literal(TDT[7][0])))
                if TDTComponents[7] >= 2:
                    g.add((Order1, n.ExcessTransportationResponsibilityCode, Literal(TDT[7][1])))
                    if TDTComponents[7] >= 3:
                        g.add((Order1, n.CustomerShipmentAuthorizationIdentifier, Literal(TDT[7][2])))
        if TDTElements >= 9:
            if TDTComponents[8] >= 1:
                g.add((Order1, n.TransportMeansIdentificationNameIdentifier, Literal(TDT[8][0])))
                if TDTComponents[8] >= 2:
                    g.add((Order1, n.CodeListIdentificationCode, Literal(TDT[8][1])))
                    if TDTComponents[8] >= 3:
                        g.add((Order1, n.CodeListResponsibleAgencyCod, Literal(TDT[8][2])))
                        if TDTComponents[8] >= 4:
                            g.add((Order1, n.TransportMeansIdentificationName, Literal(TDT[8][3])))
                            if TDTComponents[8] >= 5:
                                g.add((Order1, n.TransportMeansNationalityCode, Literal(TDT[8][4])))
        if TDTElements >= 10:
            g.add((Order1, n.TransportMeansOwnershipIndicatorCode, Literal(TDT[9][0])))
        if TDTElements >= 11:
            if TDTComponents[10] >= 1:
                g.add((Order1, n.PowerTypeCode, Literal(TDT[10][0])))
                if TDTComponents[10] >= 2:
                    g.add((Order1, n.CodeListIdentificationCode, Literal(TDT[10][1])))
                    if TDTComponents[10] >= 3:
                        g.add((Order1, n.CodeListResponsibleAgencyCod, Literal(TDT[10][2])))
                        if TDTComponents[10] >= 4:
                            g.add((Order1, n.PowerTypedescription, Literal(TDT[10][3])))


        #PAC
        if PACElements >= 2:
            g.add((Order1, n.PackagesQuantity, Literal(PAC[1][0])))
        if PACElements >= 3:
            g.add((Order1, n.PackagingLevelCode, Literal(PAC[2][0])))
            if PACComponents[2] >= 2:
                g.add((Order1, n.PackagingRelatedDescriptionCode, Literal(PAC[2][1])))
                if PACComponents[2] >= 2:
                    g.add((Order1, n.PackagingTermsAndConditionsCode, Literal(PAC[2][2])))
        if PACElements >= 4:
            g.add((Order1, n.PackageTypeDescriptionCode, Literal(PAC[3][0])))
            if PACComponents[3] >= 2:
                g.add((Order1, n.CodeListIdentificationCode, Literal(PAC[3][1])))
                if PACComponents[3] >= 2:
                    g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(PAC[3][2])))
                    if PACComponents[3] >= 3:
                        g.add((Order1, n.TypeOfPackages, Literal(PAC[3][3])))
        if PACElements >= 5:
            g.add((Order1, n.DescriptionFormatCode, Literal(PAC[4][0])))
            if PACComponents[4] >= 2:
                g.add((Order1, n.TypeOfPackages, Literal(PAC[4][1])))
                if PACComponents[4] >= 3:
                    g.add((Order1, n.ItemTypeIdentificationCode, Literal(PAC[4][2])))
                    if PACComponents[4] >= 4:
                        g.add((Order1, n.TypeOfPackages, Literal(PAC[4][3])))
                        if PACComponents[4] >= 5:
                            g.add((Order1, n.ItemTypeIdentificationCode2, Literal(PAC[4][4])))
        if PACElements >= 6:
            g.add((Order1, n.ReturnablePackageFreightPaymentResponsibilityCode, Literal(PAC[5][0])))
            if PACComponents[5] >= 2:
                g.add((Order1, n.ReturnablePackageLoadContentsCode, Literal(PAC[5][1])))


        #FII
        if FIIElements >= 2:
            g.add((Order1, n.PartyFunctionCodeQualifier, Literal(FII[1][0])))
        if FIIElements >= 3:
            if FIIComponents[2] >= 1:
                g.add((Order1, n.AccountHolderIdentifier, Literal(FII[2][0])))
                if FIIComponents[2] >= 2:
                    g.add((Order1, n.AccountHolderName, Literal(FII[2][1])))
                    if FIIComponents[2] >= 3:
                        g.add((Order1, n.AccountHolderName, Literal(FII[2][2])))
                        if FIIComponents[2] >= 4:
                            g.add((Order1, n.CurrencyIdentificationCode, Literal(FII[2][3])))
        if FIIElements >= 4:
            if FIIComponents[3] >= 1:
                g.add((Order1, n.InstitutionNameCode, Literal(FII[3][0])))
                if FIIComponents[3] >= 2:
                    g.add((Order1, n.CodeListIdentificationCode, Literal(FII[3][1])))
                    if FIIComponents[3] >= 3:
                        g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(FII[3][2])))
                        if FIIComponents[3] >= 4:
                            g.add((Order1, n.InstitutionBranchIdentifier, Literal(FII[3][3])))
                            if FIIComponents[3] >= 5:
                                g.add((Order1, n.CodeListIdentificationCode, Literal(FII[3][4])))
                                if FIIComponents[3] >= 6:
                                    g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(FII[3][5])))
                                    if FIIComponents[3] >= 7:
                                        g.add((Order1, n.InstitutionName, Literal(FII[3][6])))
                                        if FIIComponents[3] >= 8:
                                            g.add((Order1, n.InstitutionBranchLocationName, Literal(FII[3][7])))
        if FIIElements >= 5:
            g.add((Order1, n.CountryIdentifier, Literal(FII[4][0])))

        #BGM
        if BGMElements >= 2:
            g.add((Order1, n.DocumentNameCode, Literal(BGM[1][0])))
            if BGMComponents[1] >= 2:
                g.add((Order1, n.CodeListIdentificationCode, Literal(BGM[1][1])))
                if BGMComponents[1] >= 3:
                    g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(BGM[1][2])))
                    if BGMComponents[1] >= 4:
                        g.add((Order1, n.DocumentName, Literal(BGM[1][3])))
        if BGMElements >= 3:
            g.add((Order1, n.DocumentIdentifier, Literal(BGM[2][0])))
            if BGMComponents[2] >= 2:
                g.add((Order1, n.VersionIdentifier, Literal(BGM[2][1])))
                if BGMComponents[2] >= 3:
                    g.add((Order1, n.RevisionIdentifier, Literal(BGM[2][2])))
        if BGMElements >= 4:
            g.add((Order1, n.MessageFunctionCode, Literal(BGM[3][0])))
        if BGMElements >= 5:
            g.add((Order1, n.ResponseTypeCode, Literal(BGM[4][0])))
        if BGMElements >= 6:
            g.add((Order1, n.DocumentStatusCode, Literal(BGM[5][0])))
        if BGMElements >= 7:
            g.add((Order1, n.LanguageNameCode, Literal(BGM[6][0])))

        #MEA
        if MEAElements >= 2:
            g.add((Order1, n.MeasurementPurposeCodeQualifier, Literal(MEA[1][0])))
        if MEAElements >= 3:
            if MEAComponents[2] >= 1:
                g.add((Order1, n.MeasuredAttributeCode, Literal(MEA[2][0])))
                if MEAComponents[2] >= 2:
                    g.add((Order1, n.MeasurementSignificanceCode, Literal(MEA[2][1])))
                    if MEAComponents[2] >= 3:
                        g.add((Order1, n.NonDiscreteMeasurementNameCode, Literal(MEA[2][2])))
                        if MEAComponents[2] >= 4:
                            g.add((Order1, n.NonDiscreteMeasurementName, Literal(MEA[2][3])))
        if MEAElements >= 4:
            if MEAComponents[3] >= 1:
                g.add((Order1, n.MeasurementUnitCode, Literal(MEA[3][0])))
                if MEAComponents[3] >= 2:
                    g.add((Order1, n.Measure, Literal(MEA[3][1])))
                    if MEAComponents[3] >= 3:
                        g.add((Order1, n.RangeMinimumQuantity, Literal(MEA[3][2])))
                        if MEAComponents[3] >= 4:
                            g.add((Order1, n.RangeMaximumQuantity, Literal(MEA[3][3])))
                            if MEAComponents[3] >= 5:
                                g.add((Order1, n.SignigicantDigitsQuantity, Literal(MEA[3][3])))
        if MEAElements >= 5:
            g.add((Order1, n.SurfaceOrLayerCode, Literal(MEA[4][0])))

        #CUX
        if CUXElements >= 2:
            if CUXComponents[1] >= 1:
                g.add((Order1, n.CurrencyUsageCodeQualifier, Literal(CUX[1][0])))
                if CUXComponents[1] >= 2:
                    g.add((Order1, n.CurrencyIdentificationCode, Literal(CUX[1][1])))
                    if CUXComponents[1] >= 3:
                        g.add((Order1, n.CurrencyTypeCodeQualifier, Literal(CUX[1][2])))
                        if CUXComponents[1] >= 4:
                            g.add((Order1, n.CurrencyRate, Literal(CUX[1][3])))
        if CUXElements >= 3:
            if CUXComponents[2] >= 1:
                g.add((Order1, n.CurrencyUsageCodeQualifier, Literal(CUX[2][0])))
                if CUXComponents[2] >= 2:
                    g.add((Order1, n.CurrencyIdentificationCode, Literal(CUX[2][1])))
                    if CUXComponents[2] >= 3:
                        g.add((Order1, n.CurrencyTypeCodeQualifier, Literal(CUX[2][2])))
                        if CUXComponents[2] >= 4:
                            g.add((Order1, n.CurrencyRate, Literal(CUX[2][3])))
        if CUXElements >= 4:
            g.add((Order1, n.CurrencyExchangeRate, Literal(CUX[3][0])))
        if CUXElements >= 5:
            g.add((Order1, n.ExchangeRateCurrencyMarketIdentifier, Literal(CUX[4][0])))

        #PYT
        if PYTElements >= 2:
            g.add((Order1, n.PaymentTermsTypeCodeQualifier, Literal(PYT[1][0])))
        if PYTElements >= 3:
            if PYTComponents[2] >= 1:
                g.add((Order1, n.PaymentTermsDescriptionIdentifier, Literal(PYT[2][0])))
                if PYTComponents[2] >= 2:
                    g.add((Order1, n.CodeListIdentificationCode, Literal(PYT[2][1])))
                    if PYTComponents[2] >= 3:
                        g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(PYT[2][2])))
                        if PYTComponents[2] >= 4:
                            g.add((Order1, n.PaymentTermsDescription, Literal(PYT[2][3])))
        if PYTElements >= 4:
            g.add((Order1, n.EventTimeReferenceCode, Literal(PYT[3][0])))
        if PYTElements >= 5:
            g.add((Order1, n.TermsTimeRelationCode, Literal(PYT[4][0])))
        if PYTElements >= 6:
            g.add((Order1, n.PeriodTypeCode, Literal(PYT[5][0])))
        if PYTElements >= 7:
            g.add((Order1, n.PeriodCountQuantity, Literal(PYT[6][0])))

        #DTM

        if DTMElements >= 2:
            g.add((Order1, n.DateOrTimeOrPeriodFunctionCodeQualifier, Literal(DTM[1][0])))
            if DTMComponents[1] >= 2:
                g.add((Order1, n.DateOrTimeOrPeriodText, Literal(DTM[1][1])))
                if DTMComponents[1] >= 3:
                    g.add((Order1, n.DateOrTimeOrPeriodFormatCode, Literal(DTM[1][2])))

        #FTX
        if FTXElements >= 2:
            g.add((Order1, n.TextSubjectCodeQualifier, Literal(FTX[1][0])))
        if FTXElements >= 3:
            g.add((Order1, n.FreeTextFunctionCode, Literal(FTX[2][0])))
        if FTXElements >= 4:
            g.add((Order1, n.FreeTextDescriptionCode, Literal(FTX[3][0])))
            if FTXComponents[3] >= 2:
                g.add((Order1, n.CodeListIdentificationCode, Literal(FTX[3][1])))
                if FTXComponents[3] >= 3:
                    g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(FTX[3][2])))
        if FTXElements >= 5:
            g.add((Order1, n.FreeText, Literal(FTX[4][0])))
            if FTXComponents[4] >= 2:
                g.add((Order1, n.FreeText, Literal(FTX[4][1])))
                if FTXComponents[4] >= 3:
                    g.add((Order1, n.FreeText, Literal(FTX[4][2])))
                    if FTXComponents[4] >= 4:
                        g.add((Order1, n.FreeText, Literal(FTX[4][3])))
                        if FTXComponents[4] >= 5:
                            g.add((Order1, n.FreeText, Literal(FTX[4][4])))
        if FTXElements >= 6:
            g.add((Order1, n.LanguageNameCode, Literal(FTX[5][0])))
        if FTXElements >= 7:
            g.add((Order1, n.FreeTextFormatCode, Literal(FTX[6][0])))

        #RFF
        if RFFElements >= 2:
            g.add((Order1, n.ReferenceCodeQualifier, Literal(RFF[1][0])))
            if RFFComponents >= 2:
                g.add((Order1, n.ReferenceIdentifier, Literal(RFF[1][1])))
                if RFFComponents >= 3:
                    g.add((Order1, n.DocumentLineIdentifier, Literal(RFF[1][2])))
                    if RFFComponents >= 4:
                        g.add((Order1, n.VersionIdentifier, Literal(RFF[1][3])))
                        if RFFComponents >= 5:
                            g.add((Order1, n.RevisionIdentifier, Literal(RFF[1][4])))

        #TOD
        if TODElements >= 2:
            g.add((Order1, n.DeliveryOrTransportTermsFunctionCode, Literal(TOD[1][0])))
        if TODElements >= 3:
            g.add((Order1, n.TransportChargesPaymentMethodCode, Literal(TOD[2][0])))
        if TODElements >= 4:
            if TODComponents[3] >= 1:
                g.add((Order1, n.DeliveryOrTransportTermsDescriptionCode, Literal(TOD[3][0])))
                if TODComponents[3] >= 1:
                    g.add((Order1, n.CodeListIdentificationCode, Literal(TOD[3][1])))
                    if TODComponents[3] >= 3:
                        g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(TOD[3][2])))
                        if TODComponents[3] >=4:
                            g.add((Order1, n.DeliveryOrTransportTermsDescription, Literal(TOD[3][3])))
                            if TODComponents[3] >= 5:
                                g.add((Order1, n.DeliveryOrTransportTermsDescription, Literal(TOD[3][4])))


        #NAD
        if NADElements >= 2:
            g.add((Order1, n.PartyFunctionCodeQualifier, Literal(NAD[1][0])))
        if NADElements >= 3:
            g.add((Order1, n.PartyIdentifier, Literal(NAD[2][0])))
            if NADComponents[2] >= 2:
                g.add((Order1, n.CodeListIdentificationCode, Literal(NAD[2][1])))
                if NADComponents[2] == 3:
                    g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(NAD[2][2])))
        if NADElements >= 4:
            g.add((Order1, n.NameAndAdressDescription, Literal(NAD[3][0])))
            if NADComponents[3] >= 2:
                g.add((Order1, n.NameAndAdressDescription, Literal(NAD[3][1])))
                if NADComponents[3] >= 3:
                    g.add((Order1, n.NameAndAdressDescription, Literal(NAD[3][2])))
                    if NADComponents[3] >= 4:
                        g.add((Order1, n.NameAndAdressDescription, Literal(NAD[3][3])))
                        if NADComponents[3] >= 5:
                            g.add((Order1, n.NameAndAdressDescription, Literal(NAD[3][4])))
        if NADElements >= 5:
            g.add((Order1, n.PartyName, Literal(NAD[4][0])))
            if NADComponents[4] >= 2:
                g.add((Order1, n.PartyName, Literal(NAD[4][1])))
                if NADComponents[4] >= 3:
                    g.add((Order1, n.PartyName, Literal(NAD[4][2])))
                    if NADComponents[4] >= 4:
                        g.add((Order1, n.PartyName, Literal(NAD[4][3])))
                        if NADComponents[4] >= 5:
                            g.add((Order1, n.PartyName, Literal(NAD[4][4])))
                            if NADComponents[4] >= 6:
                                g.add((Order1, n.PartyNameFormatCode, Literal(NAD[4][5])))
        if NADElements >= 6:
            g.add((Order1, n.StreetAndNumberOrPostOfficeBoxIdentifier, Literal(NAD[5][0])))
            if NADComponents[5] >= 2:
                g.add((Order1, n.StreetAndNumberOrPostOfficeBoxIdentifier, Literal(NAD[5][1])))
                if NADComponents[5] >= 3:
                    g.add((Order1, n.StreetAndNumberOrPostOfficeBoxIdentifier, Literal(NAD[5][2])))
                    if NADComponents[5] >= 4:
                        g.add((Order1, n.StreetAndNumberOrPostOfficeBoxIdentifier, Literal(NAD[5][3])))
        if NADElements >= 7:
            g.add((Order1, n.CityName, Literal(NAD[6][0])))
        if NADElements >= 8:
            g.add((Order1, n.CountrySubdivisionIdentifier, Literal(NAD[7][0])))
            if NADComponents[7] >= 2:
                g.add((Order1, n.CodeListIdentificationCode, Literal(NAD[7][1])))
                if NADComponents[7] >= 3:
                    g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(NAD[7][2])))
                    if NADComponents[7] >= 4:
                        g.add((Order1, n.CountrySubdivisionName, Literal(NAD[7][3])))
        if NADElements >= 9:
            g.add((Order1, n.PostalIdentificationCode, Literal(NAD[8][0])))
        if NADElements >= 10:
            g.add((Order1, n.CountryIdentifier, Literal(NAD[9][0])))

        #GIR
        if GIRElements >= 2:
            g.add((Order1, n.SetTypeCodeQualifier, Literal(GIR[1][0])))
        if GIRElements >= 3:
            g.add((Order1, n.ObjectIdentifier, Literal(GIR[2][0])))
            if GIRComponents[2] >= 2:
                g.add((Order1, n.ObjectIdentificationCodeQualifier, Literal(GIR[2][1])))
                if GIRComponents[2] >= 3:
                    g.add((Order1, n.StatusDescriptionCode, Literal(GIR[2][2])))
        if GIRElements >= 4:
            g.add((Order1, n.ObjectIdentifier, Literal(GIR[3][0])))
            if GIRComponents[2] >= 2:
                g.add((Order1, n.ObjectIdentificationCodeQualifier, Literal(GIR[3][1])))
                if GIRComponents[2] >= 3:
                    g.add((Order1, n.StatusDescriptionCode, Literal(GIR[3][2])))
        if GIRElements >= 5:
            g.add((Order1, n.ObjectIdentifier, Literal(GIR[4][0])))
            if GIRComponents[2] >= 2:
                g.add((Order1, n.ObjectIdentificationCodeQualifier, Literal(GIR[4][1])))
                if GIRComponents[2] >= 3:
                    g.add((Order1, n.StatusDescriptionCode, Literal(GIR[4][2])))
        if GIRElements >= 6:
            g.add((Order1, n.ObjectIdentifier, Literal(GIR[5][0])))
            if GIRComponents[2] >= 2:
                g.add((Order1, n.ObjectIdentificationCodeQualifier, Literal(GIR[5][1])))
                if GIRComponents[2] >= 3:
                    g.add((Order1, n.StatusDescriptionCode, Literal(GIR[5][2])))
        if GIRElements >= 7:
            g.add((Order1, n.ObjectIdentifier, Literal(GIR[6][0])))
            if GIRComponents[2] >= 2:
                g.add((Order1, n.ObjectIdentificationCodeQualifier, Literal(GIR[6][1])))
                if GIRComponents[2] >= 3:
                    g.add((Order1, n.StatusDescriptionCode, Literal(GIR[6][2])))

        #LIN
        if LINElements >= 2:
            g.add((Order1, n.LineItemIdentifier , Literal(LIN[1][0])))
        if LINElements >= 3:
            g.add((Order1, n.ActionCode, Literal(LIN[2][0])))


        if LINElements >= 4:
            #g.add((Order1, n.ItemIdentifier, n.Product3))
            #g.add((n.Product3, n.ItemIdentifier, Literal(LIN[3][0])))
            #g.add((n.Product3, n.ItemAmount, n.Amount))
            #g.add((n.Product3, n.ItemPrice, n.Price))
            g.add((Order1, n.ItemIdentifier, Literal(LIN[3][0])))
            if LINComponents[3] >= 2:
                g.add((Order1, n.ItemTypeIdentificationCode, Literal(LIN[3][1])))
                if LINComponents[3] >= 3:
                    g.add((Order1, n.CodeListIdentificationCode, Literal(LIN[3][2])))
                    if LINComponents[3] >= 4:
                        g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(LIN[3][3])))

        if LINElements >= 5:
            g.add((Order1, n.SubLineIndicatorCode , Literal(LIN[4][0])))
            if LINComponents[4] >= 2:
                g.add((Order1, n.LineItemIdentifier, Literal(LIN[4][1])))
        if LINElements >= 6:
            g.add((Order1, n.ConfigurationLevelNumber , Literal(LIN[5][0])))
        if LINElements >= 7:
            g.add((Order1, n.ConfigurationOperationCode , Literal(LIN[6][0])))

        #QTY

        if QTYElements >= 2:
            g.add((Order1, n.QuantityTypeCodeQualifier, Literal(QTY[1][0])))
            if QTYComponents[1] >= 2:
                #g.add((Order1, n.Quantity, n.Amount))
                #g.add((n.Amount, n.Quantity, Literal(QTY[1][1])))
                g.add((Order1, n.Quantity, Literal(QTY[1][1])))
                if QTYComponents[1] >= 3:
                    g.add((Order1, n.MeasurementUnitCode, Literal(QTY[1][2])))

        #RJL
        if RJLElements >= 2:
            g.add((Order1, n.AccountingJournalIdentifier, Literal(RJL[1][0])))
            if RJLComponents[1] >= 2:
                g.add((Order1, n.CodeListIdentificationCode, Literal(RJL[1][1])))
                if RJLComponents[1] >= 3:
                    g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(RJL[1][2])))
                    if RJLComponents[1] >= 4:
                      g.add((Order1, n.AccountingJournalName, Literal(RJL[1][3])))
        if RJLElements >= 3:
            g.add((Order1, n.AccountingEntryTypeNameCode, Literal(RJL[2][0])))
            if RJLComponents[2] >= 2:
                g.add((Order1, n.CodeListIdentificationCode, Literal(RJL[2][1])))
                if RJLComponents[2] >= 3:
                    g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(RJL[2][2])))
                    if RJLComponents[2] >= 4:
                      g.add((Order1, n.AccountingEntryTypeName, Literal(RJL[2][3])))




        #PRI
        if PRIElements >= 2:
            g.add((Order1, n.PriceCodeQualifier, Literal(PRI[1][0])))
            if PRIComponents[1] >=2:
                g.add((Order1, n.PriceAmount, Literal(PRI[1][1])))
                if PRIComponents[1] >=3:
                    g.add((Order1, n.PriceTypeCode, Literal(PRI[1][2])))
                    if PRIComponents[1] >=4:
                        g.add((Order1, n.PriceSpecificationCode, Literal(PRI[1][3])))
                        if PRIComponents[1] >=5:
                            g.add((Order1, n.UnitPriceBasisQuantity, Literal(PRI[1][4])))
                            if PRIComponents[1] >=6:
                                g.add((Order1, n.MeasurementUnitCode, Literal(PRI[1][5])))
        if PRIElements >= 3:
            g.add((Order1, n.SubLineItemPriceChangeOperationCode, Literal(PRI[2][0])))

        # UNS
        if UNSElements >= 2:
            g.add((Order1, n.SectionIdentification, Literal(UNS[1][0])))


        #LOC
        if LOCElements >= 2:
            g.add((Order1, n.LocationFunctionCodeQualifier, Literal(LOC[1][0])))
        if LOCElements >= 3:
            if LOCComponents[2] >= 1:
                g.add((Order1, n.LocationNameCode, Literal(LOC[2][0])))
                if LOCComponents[2] >= 2:
                    g.add((Order1, n.CodeListIdentificationCode, Literal(LOC[2][1])))
                    if LOCComponents[2] >= 3:
                        g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(LOC[2][2])))
                        if LOCComponents[2] >= 4:
                            g.add((Order1, n.LocationName, Literal(LOC[2][3])))
        if LOCElements >= 4:
            if LOCComponents[3] >= 1:
                g.add((Order1, n.FirstRelatedLocationNameCode, Literal(LOC[3][0])))
                if LOCComponents[2] >= 2:
                    g.add((Order1, n.CodeListIdentificationCode, Literal(LOC[3][1])))
                    if LOCComponents[2] >= 3:
                        g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(LOC[3][2])))
                        if LOCComponents[2] >= 4:
                            g.add((Order1, n.FirstRelatedLocationName, Literal(LOC[3][3])))
        if LOCElements >= 5:
            if LOCComponents[4] >= 1:
                g.add((Order1, n.SecondRelatedLocationNameCode, Literal(LOC[4][0])))
                if LOCComponents[4] >= 2:
                    g.add((Order1, n.CodeListIdentificationCode, Literal(LOC[4][1])))
                    if LOCComponents[4] >= 3:
                        g.add((Order1, n.CodeListResponsibleAgenyCode, Literal(LOC[4][2])))
                        if LOCComponents[4] >= 4:
                            g.add((Order1, n.SecondRelatedLocationName, Literal(LOC[4][3])))
        if LOCElements >= 6:
             g.add((Order1, n.RelationCode, Literal(LOC[5][0])))
        # CNT

        if CNTElements >= 2:
            g.add((Order1, n.ControlTotalTypeCodeQualifier, Literal(CNT[1][0])))
            if CNTComponents[1] >= 2:
                g.add((Order1, n.ControlTotalQuantity, Literal(CNT[1][1])))
                if CNTComponents[1] >= 3:
                    g.add((Order1, n.MeasurementUnitCode, Literal(CNT[1][2])))



        #UNT
        if UNTElements >= 2:
            g.add((Order1,  n.NumberOfSegmentInAMessage,Literal(UNT[1])))
            g.add((Order1,  n.MessageReferenceNumber,Literal(UNT[2])))

        #PAI
        if PAIElements >= 2:
            if PAIComponents[1] >= 1:
                g.add((Order1, n.PaymentConditionsCode, Literal(PAI[1][0])))
                if PAIComponents[1] >= 2:
                    g.add((Order1, n.PaymentGuaranteeMeansCode, Literal(PAI[1][1])))
                    if PAIComponents[1] >= 3:
                        g.add((Order1, n.PaymentMeansCode, Literal(PAI[1][2])))
                        if PAIComponents[1] >= 4:
                            g.add((Order1, n.CodeListIdentificationCode, Literal(PAI[1][3])))
                            if PAIComponents[1] >= 5:
                                g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(PAI[1][4])))
                                if PAIComponents[1] >= 6:
                                    g.add((Order1, n.PaymentChannelCode, Literal(PAI[1][5])))

        #ALI
        if ALIElements >= 2:
            g.add((Order1, n.CountryOfOriginIdentifier, Literal(ALI[1][0])))
        if ALIElements >= 3:
            g.add((Order1, n.DutyRegimeTypeCode, Literal(ALI[2][0])))
        if ALIElements >= 4:
            g.add((Order1, n.SpecialConditionCode, Literal(ALI[3][0])))
        if ALIElements >= 5:
            g.add((Order1, n.CountryOfOriginNameCode, Literal(ALI[4][0])))
        if ALIElements >= 6:
            g.add((Order1, n.CountryOfOriginNameCode, Literal(ALI[5][0])))
        if ALIElements >= 7:
            g.add((Order1, n.CountryOfOriginNameCode, Literal(ALI[6][0])))
        if ALIElements >= 8:
            g.add((Order1, n.CountryOfOriginNameCode, Literal(ALI[7][0])))


        #Negar Part,21-39
        #PCD, GRP21
        if PCDElements >= 2:
            g.add((Order1, n.PercentageTypeCodeQualifier, Literal(PCD[1][0])))
            if PCDComponents[1] >= 2:
                g.add((Order1, n.Percentage, Literal(PCD[1][1])))
                if PCDComponents[1] >= 3:
                    g.add((Order1, n.PercentageBasisIdentificatonCoded, Literal(PCD[1][2])))
                    if PCDComponents[1] >= 4:
                        g.add((Order1, n.CodeListIdentification, Literal(PCD[1][3])))
                        if PCDComponents[1] >= 5:
                            g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(PCD[1][4])))
        if PCDElements >= 3:
            g.add((Order1, n.StatusDescriptionCode, Literal(PCD[2][0])))

        #MOA, GRP22
        if MOAElements >= 2:
            g.add((Order1, n.MonetaryAmountTypeCodeQualifier, Literal(MOA[1][0])))
            if MOAComponents[1] >= 2:
                g.add((Order1, n.MonetaryAmount, Literal(MOA[1][1])))
                if MOAComponents[1] >= 3:
                    g.add((Order1, n.CurrencyIdentificationCode, Literal(MOA[1][2])))
                    if MOAComponents[1] >= 4:
                       g.add((Order1, n.CurrencyTypeCodeQualifier, Literal(MOA[1][3])))
                       if MOAComponents[1] >= 5:
                           g.add((Order1, n.StatusDescriptionCode, Literal(MOA[1][4])))

         # RTE, GRP23
        if RTEElements >= 2:
            g.add((Order1, n.RateTypeCodeQualifier, Literal(RTE[1][0])))
            if RTEComponents[1] >= 2:
                g.add((Order1, n.UnitPriceBasisRate, Literal(RTE[1][1])))
                if RTEComponents[1] >= 3:
                    g.add((Order1, n.UnitPriceBasisQuantity, Literal(RTE[1][2])))
                    if RTEComponents[1] >= 4:
                        g.add((Order1, n.MeasurementUnitCode, Literal(RTE[1][3])))
        if RTEElements >= 3:
            g.add((Order1, n.StatusDescriptionCode, Literal(RTE[2][0])))

        # TAX, GRP24
        if TAXElements >= 2:
            g.add((Order1, n.DutyOrTaxOrFeeFunctionCodeQualifier, Literal(TAX[1][0])))
        if TAXElements >= 3:
            g.add((Order1, n.DutyOrTaxOrFeeTypeNameCode, Literal(TAX[2][0])))
            if TAXComponents[2] >= 2:
                g.add((Order1, n.CodeListIdentificationCode, Literal(TAX[2][1])))
                if TAXComponents[2] >= 3:
                    g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(TAX[2][2])))
                    if TAXComponents[2] >= 4:
                        g.add((Order1, n.DutyOrTaxOrFeeTypeName, Literal(TAX[2][3])))
        if TAXElements >= 4:
            g.add((Order1, n.DutyOrTaxOrFeeAccountCode, Literal(TAX[3][0])))
            if UNHComponents[3] >= 2:
                g.add((Order1, n.CodeListIdentificationCode, Literal(TAX[3][1])))
                if UNHComponents[3] >= 3:
                    g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(TAX[3][2])))
        if TAXElements >= 5:
                    g.add((Order1, n.DutyORTaxOrFeeAssessmentBasisQuantity, Literal(TAX[4][0])))
        if TAXElements >= 6:
            g.add((Order1, n.DutyOrTaxOrFeeRateCode, Literal(TAX[5][0])))
            if TAXComponents[5] >= 2:
                g.add((Order1, n.CodeListIdentificationCode, Literal(TAX[5][1])))
                if TAXComponents[5] >= 3:
                    g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(TAX[5][2])))
                    if TAXComponents[5] >= 4:
                        g.add((Order1, n.DutyOrTaxOrFeeRate, Literal(TAX[5][3])))
                        if TAXComponents[5] >= 2:
                            g.add((Order1, n.DutyOrTaxOrFeeRateBasisCode, Literal(TAX[5][4])))
                            if TAXComponents[5] >= 3:
                                g.add((Order1, n.CodeListIdentificationCode, Literal(TAX[5][5])))
                                if TAXComponents[5] >= 4:
                                    g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(TAX[5][6])))
        if TAXElements >= 7:
            g.add((Order1, n.DutyOrTaxOrFeeCategoryCode, Literal(TAX[6][0])))
        if TAXElements >= 8:
            g.add((Order1, n.PartyTaxIdentifier, Literal(TAX[7][0])))
        if TAXElements >= 9:
           g.add((Order1, n.CalculationSequenceCode, Literal(TAX[8][0])))
        if TAXElements >= 10:
           g.add((Order1, n.TaxOrDutyOrFeePaymentDueDateCode, Literal(TAX[9][0])))

        # RCS, GRP25
        if RCSElements >= 2:
            g.add((Order1, n.SectorAreaIdentificationCodeQualifier, Literal(RCS[1][0])))
        if RCSElements >= 3:
            g.add((Order1, n.RequirementOrConditionDescriptionIdentifier, Literal(RCS[2][0])))
            if RCSComponents[2] >= 2:
                g.add((Order1, n.CodeListIdentificationCode, Literal(RCS[2][1])))
                if RCSComponents[2] >= 3:
                    g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(RCS[2][2])))
                    if RCSComponents[2] >= 4:
                        g.add((Order1, n.RequirementOrConditionDescription, Literal(RCS[2][3])))
        if RCSElements >= 4:
            g.add((Order1, n.ActionCode, Literal(RCS[3][0])))
        if RCSElements >= 5:
            g.add((Order1, n.CountryIdentifier, Literal(RCS[4][0])))


        # DGS, GRP26

        if DGSElements >= 2:
            g.add((Order1, n.DangerousGoodsRegulationsCode, Literal(DGS[1][0])))
        if DGSElements >= 3:
            g.add((Order1, n.HazardIdentificationCode, Literal(DGS[2][0])))
            if DGSComponents[2] >= 2:
                g.add((Order1, n.AdditionalHazardClassificationIdentifier, Literal(DGS[2][1])))
                if DGSComponents[2] >= 3:
                    g.add((Order1, n.HazardCodeVersionIdentifier, Literal(DGS[2][2])))
        if DGSElements >= 4:
            g.add((Order1, n.UnitedNationsDangerousGoodsIdentifier, Literal(DGS[3][0])))
            if DGSComponents[3] >= 2:
                g.add((Order1, n.DangerousGoodsFlashpointDescription, Literal(DGS[3][1])))
        if DGSElements >= 5:
            g.add((Order1, n.ShipmentFlashpointDegree, Literal(DGS[4][0])))
            if DGSComponents[4] >= 2:
                g.add((Order1, n.MeasurementUnitCode, Literal(DGS[4][1])))
        if DGSElements >= 6:
            g.add((Order1, n.PackagingDangerLevelCode, Literal(DGS[5][0])))
        if DGSElements >= 7:
            g.add((Order1, n.EmergencyProcedureForShipsIdentifier, Literal(DGS[6][0])))
        if DGSElements >= 8:
            g.add((Order1, n.HazardMedicalFirstAidGuideIdentifier, Literal(DGS[7][0])))
        if DGSElements >= 9:
            g.add((Order1, n.TransportEmergencyCardIdentifier, Literal(DGS[8][0])))
        if DGSElements >= 10:
            g.add((Order1, n.OrangeHazardPlacardUpperPartIdentifier, Literal(DGS[9][0])))
            if DGSComponents[9] >= 2:
                g.add((Order1, n. OrangeHazardPlacardLowerPartIdentifier , Literal(DGS[9][1])))
        if DGSElements >= 11:
            g.add((Order1, n.DangerousGoodsMarkingIdentifier , Literal(DGS[10][0])))
            if DGSComponents[10] >= 2:
                g.add((Order1, n.DangerousGoodsMarkingIdentifier, Literal(DGS[10][1])))
                if DGSComponents[10] >= 3:
                    g.add((Order1, n.DangerousGoodsMarkingIdentifier, Literal(DGS[10][2])))
                    if DGSComponents[10] >= 4:
                        g.add((Order1, n.DangerousGoodsMarkingIdentifier, Literal(DGS[10][3])))
        if DGSElements >= 12:
            g.add((Order1, n.PackingInstructionTypeCode, Literal(DGS[11][0])))
        if DGSElements >= 13:
            g.add((Order1, n.TransportMeansDescriptionCode, Literal(DGS[12][0])))
        if DGSElements >= 14:
            g.add((Order1, n.HazardousCargoTransportAuthorisationCode, Literal(DGS[13][0])))
        if DGSElements >= 15:
            g.add((Order1, n.TunnelRestrictionCode, Literal(DGS[14][0])))
            if DGSComponents[14] >= 2:
                g.add((Order1, n.CodeListIdentificationCode, Literal(DGS[14][1])))
                if DGSComponents[14] >= 3:
                    g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(DGS[14][2])))
        #CTA, GRP27

        if CTAElements >= 2:
            g.add((Order1, n.ContactFunctionCode, Literal(CTA[1][0])))
        if CTAElements >= 3:
            g.add((Order1, n.DepartmentOrEmployeeNameCode, Literal(CTA[2][0])))
            if CTAComponents[2] >= 2:
                g.add((Order1, n.DepartmentOrEmployeeName, Literal(CTA[2][1])))

        #COM, GRP27
        if COMElements >= 2:
            g.add((Order1, n.CommunicationAddressIdentifier, Literal(COM[1][0])))
            if COMComponents[1] >= 2:
                g.add((Order1, n.CommunicationAddressCodeQualifier, Literal(COM[1][1])))

        #PIA, GRP28

        if PIAElements >= 2:
            g.add((Order1, n.ProductIdentifierCodeQualifier, Literal(PIA[1][0])))
        if PIAElements >= 3:
            g.add((Order1, n.ItemIdentifier, Literal(PIA[2][0])))
            if PIAComponents[2] >= 2:
                g.add((Order1, n.ItemTypeIdentificationCode, Literal(PIA[2][1])))
                if PIAComponents[2] >= 3:
                    g.add((Order1, n.CodeListIdentificationCode, Literal(PIA[2][2])))
                    if PIAComponents[2] >= 4:
                        g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(PIA[2][3])))
        if PIAElements >= 4:
            g.add((Order1, n.ItemIdentifier, Literal(PIA[3][0])))
            if PIAComponents[3] >= 2:
                g.add((Order1, n.ItemTypeIdentificationCode, Literal(PIA[3][1])))
                if PIAComponents[3] >= 3:
                    g.add((Order1, n.CodeListIdentificationCode, Literal(PIA[3][2])))
                    if PIAComponents[3] >= 4:
                        g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(PIA[3][3])))
        if PIAElements >= 5:
            g.add((Order1, n.ItemIdentifier, Literal(PIA[4][0])))
            if PIAComponents[4] >= 2:
                g.add((Order1, n.ItemTypeIdentificationCode, Literal(PIA[4][1])))
                if PIAComponents[4] >= 3:
                    g.add((Order1, n.CodeListIdentificationCode, Literal(PIA[4][2])))
                    if PIAComponents[4] >= 4:
                        g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(PIA[4][3])))
        if PIAElements >= 6:
            g.add((Order1, n.ItemIdentifier, Literal(PIA[5][0])))
            if PIAComponents[5] >= 2:
                g.add((Order1, n.ItemTypeIdentificationCode, Literal(PIA[5][1])))
                if PIAComponents[5] >= 3:
                    g.add((Order1, n.CodeListIdentificationCode, Literal(PIA[5][2])))
                    if PIAComponents[5] >= 4:
                        g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(PIA[5][3])))
        if PIAElements >= 7:
            g.add((Order1, n.ItemIdentifier, Literal(PIA[6][0])))
            if PIAComponents[6] >= 2:
                g.add((Order1, n.ItemTypeIdentificationCode, Literal(PIA[6][1])))
                if PIAComponents[6] >= 3:
                    g.add((Order1, n.CodeListIdentificationCode, Literal(PIA[6][2])))
                    if PIAComponents[6] >= 4:
                        g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(PIA[6][3])))

        #GEI, GRP28

        if GEIElements >= 2:
            g.add((Order1, n.ProcessingInformationCodeQualifier, Literal(GEI[1][0])))
        if GEIElements >= 3:
            g.add((Order1, n.ProcessingIndicatorDescriptionCode, Literal(GEI[2][0])))
            if GEIComponents[2] >= 2:
                g.add((Order1, n. CodeListIdentificationCode , Literal(GEI[2][1])))
                if GEIComponents[2] >= 3:
                    g.add((Order1, n.CodeListResponsibleAagencyCode, Literal(GEI[2][2])))
                    if GEIComponents[2] >= 4:
                        g.add((Order1, n.ProcessingIndicatorDescription, Literal(GEI[2][3])))
        if GEIElements >= 4:
            g.add((Order1, n.ProcessTypeDescriptionCode, Literal(GEI[3][0])))

        #GIN, GRP28

        if GINElements >= 2:
            g.add((Order1, n.ObjectIdentificationCodeQualifier, Literal(GIN[1][0])))
        if GINElements >= 3:
            g.add((Order1, n.ObjectIdentifier, Literal(GIN[2][0])))
            if GINComponents[2] >= 2:
                g.add((Order1, n.ObjectIdentifier, Literal(GIN[2][1])))
        if GINElements >= 4:
            g.add((Order1, n.ObjectIdentifier, Literal(GIN[3][0])))
            if GINComponents[3] >= 2:
                g.add((Order1, n.ObjectIdentifier, Literal(GIN[3][1])))
        if GINElements >= 5:
            g.add((Order1, n.ObjectIdentifier, Literal(GIN[4][0])))
            if GINComponents[4] >= 2:
                g.add((Order1, n.ObjectIdentifier, Literal(GIN[4][1])))
        if GINElements >= 6:
            g.add((Order1, n.ObjectIdentifier, Literal(GIN[5][0])))
            if GINComponents[5] >= 2:
                g.add((Order1, n.ObjectIdentifier, Literal(GIN[5][1])))
        if GINElements >= 7:
            g.add((Order1, n.ObjectIdentifier, Literal(GIN[6][0])))
            if GINComponents[6] >= 2:
                g.add((Order1, n.ObjectIdentifier, Literal(GIN[6][1])))

        #EQD
        if EQDElements >= 2:
            g.add((Order1, n.EquipmentTypeCodeQualifier, Literal(EQD[1][0])))
        if EQDElements >= 3:
            if EQDComponents[2] >= 1:
                g.add((Order1, n.EquipmentIdentifier, Literal(EQD[2][0])))
                if EQDComponents[2] >= 2:
                    g.add((Order1, n.CodeListIdentificationCode, Literal(EQD[2][1])))
                    if EQDComponents[2] >= 3:
                        g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(EQD[2][2])))
                        if EQDComponents[2] >= 4:
                            g.add((Order1, n.CountryIdentifier, Literal(EQD[2][3])))
        if EQDElements >= 4:
            if EQDComponents[3] >= 1:
                g.add((Order1, n.EquipmentSizeAndTypeDescriptionCode, Literal(EQD[3][0])))
                if EQDComponents[3] >= 2:
                    g.add((Order1, n.CodeListIdentificationCode, Literal(EQD[3][1])))
                    if EQDComponents[3] >= 3:
                        g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(EQD[3][2])))
                        if EQDComponents[3] >= 4:
                            g.add((Order1, n.EquipmentSizeAndTypeDescription, Literal(EQD[3][3])))
        if EQDElements >= 5:
            g.add((Order1, n.EquipmentSupplierCode, Literal(EQD[4][0])))
        if EQDElements >= 6:
            g.add((Order1, n.EquipmentStatusCode, Literal(EQD[5][0])))
        if EQDElements >= 7:
            g.add((Order1, n.FullOrEmptyIndicatorCode, Literal(EQD[6][0])))
        if EQDElements >= 8:
            g.add((Order1, n.MarkingInstructionsCode, Literal(EQD[7][0])))
        # QVR, GRP28

        if QVRElements >= 2:
            g.add((Order1, n.VarianceQuantity, Literal(QVR[1][0])))
            if QVRComponents[1] >= 2:
                g.add((Order1, n.QuantityTypeCodeQualifier, Literal(QVR[1][1])))
        if QVRElements >= 3:
            g.add((Order1, n.DiscrepancyNatureIdentificationCode, Literal(QVR[2][0])))
        if QVRElements >= 4:
                g.add((Order1, n.ChangeReasonDescriptionCode, Literal(QVR[3][0])))
                if QVRComponents[3] >= 2:
                    g.add((Order1, n.CodeListIdentificationCode, Literal(QVR[3][1])))
                    if QVRComponents[3] >= 3:
                        g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(QVR[3][2])))
                        if QVRComponents[3] >= 4:
                            g.add((Order1, n.ChangeReasonDescription, Literal(QVR[3][3])))


         # DOC, GRP28

        if DOCElements >= 2:
            g.add((Order1, n.DocumentNameCode, Literal(DOC[1][0])))
            if DOCComponents[1] >= 2:
                g.add((Order1, n.CodeListIdentificationCode, Literal(DOC[1][1])))
                if DOCComponents[1] >= 3:
                    g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(DOC[1][2])))
                    if DOCComponents[1] >= 4:
                        g.add((Order1, n.DocumentName, Literal(DOC[1][3])))

        if DOCElements >= 3:
            g.add((Order1, n.DocumentIdentifier, Literal(DOC[2][0])))
            if DOCComponents[2] >= 2:
                g.add((Order1, n.DocumentStatusCode, Literal(DOC[2][1])))
                if DOCComponents[2] >= 3:
                    g.add((Order1, n.DocumentSourceDescription, Literal(DOC[2][2])))
                    if DOCComponents[2] >= 4:
                        g.add((Order1, n.LanguageNameCode, Literal(DOC[2][3])))
                        if DOCComponents[2] >= 5:
                            g.add((Order1, n.VersionIdentifier, Literal(DOC[2][4])))
                            if DOCComponents[2] >= 6:
                                g.add((Order1, n.RevisionIdentifier, Literal(DOC[2][5])))
        if DOCElements >= 4:
            g.add((Order1, n.CommunicationMediumTypeCode, Literal(DOC[3][0])))
        if DOCElements >= 5:
            g.add((Order1, n.DocumentCopiesRequiredQuantity, Literal(DOC[4][0])))
        if DOCElements >= 6:
            g.add((Order1, n.DocumentOriginalsRequiredQuantity, Literal(DOC[5][0])))

        # MTD, GRP28

        if MTDElements >= 2:
            g.add((Order1, n.ObjectTypeCodeQualifier, Literal(MTD[1][0])))
        if MTDElements >= 3:
            g.add((Order1, n.MaintenanceOperationCode, Literal(MTD[2][0])))
        if MTDElements >= 4:
            g.add((Order1, n.MaintenanceOperationOperatorCode, Literal(MTD[3][0])))
        if MTDElements >= 5:
            g.add((Order1, n.MaintenanceOperationPayerCode, Literal(MTD[4][0])))


        #CCI, GRP29

        if CCIElements >= 2:
            g.add((Order1, n.ClassTypeCode, Literal(CCI[1][0])))
        if CCIElements >= 3:
            g.add((Order1, n.MeasuredAttributeCode, Literal(CCI[2][0])))
            if CCIComponents[2] >= 2:
                g.add((Order1, n.MeasurementSignificanceCode, Literal(CCI[2][1])))
                if CCIComponents[2] >= 3:
                    g.add((Order1, n.NonDiscreteMeasurementNameCode, Literal(CCI[2][2])))
                    if CCIComponents[2] >= 4:
                        g.add((Order1, n.NonDiscreteMeasurementName, Literal(CCI[2][3])))
        if CCIElements >= 4:
            g.add((Order1, n.CharacteristicDescriptionCode, Literal(CCI[3][0])))
            if CCIComponents[3] >= 2:
                g.add((Order1, n.CodeListIdentificationCode, Literal(CCI[3][1])))
                if CCIComponents[3] >= 3:
                    g.add((Order1, n.CodeListResponsibleAgencyCode , Literal(CCI[3][2])))
                    if CCIComponents[3] >= 4:
                        g.add((Order1, n.CharacteristicDescription, Literal(CCI[3][3])))
                        if CCIComponents[3] >= 5:
                            g.add((Order1, n.CharacteristicDescription, Literal(CCI[3][4])))
        if CCIElements >= 5:
            g.add((Order1, n.CharacteristicRelevanceCode, Literal(CCI[4][0])))

        #CAV, GRP29

        if CAVElements >= 4:
            g.add((Order1, n.CharacteristicValueDescriptionCode, Literal(CAV[3][0])))
            if CAVComponents[3] >= 2:
                g.add((Order1, n.CodeListIdentificationCode, Literal(CAV[3][1])))
                if CAVComponents[3] >= 3:
                    g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(CAV[3][2])))
                    if CAVComponents[3] >= 4:
                        g.add((Order1, n.CharacteristicValueDescription, Literal(CAV[3][3])))
                        if CAVComponents[3] >= 5:
                            g.add((Order1, n.CharacteristicValueDescription, Literal(CAV[3][4])))

        #PRI, GRP32

        if PRIElements >= 2:
            g.add((Order1, n.PriceCodeQualifier, Literal(PRI[1][0])))
            if PRIComponents[1] >= 2:
                #g.add((Order1, n.PriceAmount, n.Price))
                #g.add((n.Price, n.PriceAmount, Literal(PRI[1][1])))
                g.add((Order1, n.PriceAmount, Literal(PRI[1][1])))
                if PRIComponents[1] >= 3:
                    g.add((Order1, n.PriceTypeCode, Literal(PRI[1][2])))
                    if PRIComponents[1] >= 4:
                        g.add((Order1, n.PriceSpecificationCode, Literal(PRI[1][3])))
                        if PRIComponents[1] >= 5:
                            g.add((Order1, n.UnitPriceBasisQuantity, Literal(PRI[1][4])))
                            if PRIComponents[1] >= 6:
                                g.add((Order1, n.MeasurementUnitCode, Literal(PRI[1][5])))
        if PRIElements >= 3:
            g.add((Order1, n.SubLineItemPriceChangeOperationCode, Literal(PRI[2][0])))


        #PCI, GRP36
        if PCIElements >= 2:
            g.add((Order1, n.MarkingInstructionsCode, Literal(PCI[1][0])))
        if PCIElements >= 3:
                g.add((Order1, n.ShippingMarksDescription, Literal(PCI[2][0])))
                if PCIComponents[2] >= 2:
                    g.add((Order1, n.ShippingMarksDescription, Literal(PCI[2][1])))
                    if PCIComponents[2] >= 3:
                        g.add((Order1, n.ShippingMarksDescription, Literal(PCI[2][2])))
                        if PCIComponents[2] >= 4:
                            g.add((Order1, n.ShippingMarksDescription, Literal(PCI[2][3])))
                            if PCIComponents[2] >= 5:
                                g.add((Order1, n.ShippingMarksDescription, Literal(PCI[2][4])))
                                if PCIComponents[2] >= 6:
                                    g.add((Order1, n.ShippingMarksDescription, Literal(PCI[2][5])))
                                    if PCIComponents[2] >= 7:
                                        g.add((Order1, n.ShippingMarksDescription, Literal(PCI[2][6])))
                                        if PCIComponents[2] >= 8:
                                            g.add((Order1, n.ShippingMarksDescription, Literal(PCI[2][7])))
                                            if PCIComponents[2] >= 9:
                                                g.add((Order1, n.ShippingMarksDescription, Literal(PCI[2][8])))
                                                if PCIComponents[2] >= 10:
                                                    g.add((Order1, n.ShippingMarksDescription, Literal(PCI[2][9])))

        if PCIElements >= 4:
            g.add((Order1, n.FullOrEmptyIndicatorCode, Literal(PCI[3][0])))
        if PCIElements >= 5:
                g.add((Order1, n.MarkingTypeCode, Literal(PCI[4][0])))
                if PCIComponents[4] >= 2:
                    g.add((Order1, n.CodeListIdentificationCode, Literal(PCI[4][1])))
                    if PCIComponents[4] >= 3:
                        g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(PCI[4][2])))

        #40-60

        # DOC
        if DOCElements >= 2:
            if DOCComponents[1] >= 1:
                g.add((Order1, n.DocumentNameCode, Literal(DOC[1][0])))
                if DOCComponents[1] >= 2:
                    g.add((Order1, n.CodeListIdentificationCode, Literal(DOC[1][1])))
                    if DOCComponents[1] >= 3:
                        g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(DOC[1][2])))
                        if DOCComponents[1] >= 4:
                            g.add((Order1, n.DocumentName, Literal(DOC[1][3])))
        if DOCElements >= 3:
            if DOCComponents[2] >= 1:
                g.add((Order1, n.DocumentIdentifier, Literal(DOC[2][0])))
                if DOCComponents[2] >= 2:
                    g.add((Order1, n.DocumentStatusCode, Literal(DOC[2][1])))
                    if DOCComponents[2] >= 3:
                        g.add((Order1, n.DocumentSourceDescription, Literal(DOC[2][2])))
                        if DOCComponents[2] >= 4:
                            g.add((Order1, n.LanguageNameCode, Literal(DOC[2][3])))
                            if DOCComponents[2] >= 5:
                                g.add((Order1, n.VersionIdentifier, Literal(DOC[2][4])))
                                if DOCComponents[2] >= 6:
                                    g.add((Order1, n.RevisionIdentifier, Literal(DOC[2][5])))
        if DOCElements >= 4:
            g.add((Order1, n.CommunicationMediumTypeCode, Literal(DOC[3][0])))
        if DOCElements >= 5:
            g.add((Order1, n.DocumentCopiesRequiredQuantity, Literal(DOC[4][0])))
        if DOCElements >= 6:
            g.add((Order1, n.DocumentOriginalsRequiredQuantity, Literal(DOC[5][0])))

        # CTA
        if CTAElements >= 2:
            g.add((Order1, n.ContactFunctionCode, Literal(CTA[1][0])))
        if CTAElements >= 3:
            if CTAComponents[2] >= 1:
                g.add((Order1, n.ContactIdentifier, Literal(CTA[2][0])))
                if CTAComponents[2] >= 2:
                    g.add((Order1, n.ContactName, Literal(CTA[2][1])))
        # COM
        if COMElements >= 2:
            if COMComponents[1] >= 1:
                g.add((Order1, n.CommunicationAddressIdentifier, Literal(COM[1][0])))
                if COMComponents[1] >= 2:
                    g.add((Order1, n.CommunicationMeansTypeCode, Literal(DOC[1][1])))

        # ALC
        if ALCElements >= 2:
            g.add((Order1, n.AllowanceOrChargeCodeQualifier, Literal(ALC[1][0])))
        if ALCElements >= 3:
            g.add((Order1, n.AllowanceOrChargeIdentifier, Literal(ALC[2][0])))
            if ALCComponents[2] >= 2:
                g.add((Order1, n.AllowanceOrChargeIdentificationCode, Literal(ALC[2][1])))
        if ALCElements >= 4:
            g.add((Order1, n.SettlementMeansCode, Literal(ALC[3][0])))
        if ALCElements >= 5:
            g.add((Order1, n.CalculationSequenceCode, Literal(ALC[4][0])))
        if ALCElements >= 6:
            g.add((Order1, n.SpecialServiceDescriptionCode, Literal(ALC[5][0])))
            if ALCComponents[5] >= 2:
                g.add((Order1, n.CodeListIdentificationCode, Literal(ALC[5][1])))
                if ALCComponents[5] >= 3:
                    g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(ALC[5][2])))
                    if ALCComponents[5] >= 4:
                        g.add((Order1, n.SpecialServiceDescription, Literal(ALC[5][3])))
                        if ALCComponents[5] >= 5:
                            g.add((Order1, n.SpecialServiceDescription, Literal(ALC[5][4])))

        # EQD
        if EQDElements >= 2:
            g.add((Order1, n.EquipmentTypeCodeQualifier, Literal(EQD[1][0])))
        if EQDElements >= 3:
            if EQDComponents[2] >= 1:
                g.add((Order1, n.EquipmentIdentifier, Literal(EQD[2][0])))
                if EQDComponents[2] >= 2:
                    g.add((Order1, n.CodeListIdentificationCode, Literal(EQD[2][1])))
                    if EQDComponents[2] >= 3:
                        g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(EQD[2][2])))
                        if EQDComponents[2] >= 4:
                            g.add((Order1, n.CountryNameCode, Literal(EQD[2][3])))
        if EQDElements >= 4:
            if EQDComponents[3] >= 1:
                g.add((Order1, n.EquipmentSizeAndTypeDescriptionCode, Literal(EQD[3][0])))
                if EQDComponents[3] >= 2:
                    g.add((Order1, n.CodeListIdentificationCode, Literal(EQD[3][1])))
                    if EQDComponents[3] >= 3:
                        g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(EQD[3][2])))
                        if EQDComponents[3] >= 4:
                            g.add((Order1, n.EquipmentSizeAndTypeDescription, Literal(EQD[3][3])))
        if EQDElements >= 5:
            g.add((Order1, n.EquipmentSupplierCode, Literal(EQD[4][0])))
        if EQDElements >= 6:
            g.add((Order1, n.EquipmentStatusCode, Literal(EQD[5][0])))
        if EQDElements >= 7:
            g.add((Order1, n.FullOrEmptyIndicatorCode, Literal(EQD[6][0])))

        # HAN
        if HANElements >= 2:
            if HANComponents[1] >= 1:
                g.add((Order1, n.HandlingInstructionDescriptionCode, Literal(HAN[1][0])))
                if HANComponents[1] >= 2:
                    g.add((Order1, n.CodeListIdentificationCode, Literal(HAN[1][1])))
                    if HANComponents[1] >= 3:
                        g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(HAN[1][2])))
                        if HANComponents[1] >= 4:
                            g.add((Order1, n.HandlingInstructionDescription, Literal(HAN[1][3])))
        if HANElements >= 3:
            if HANComponents[2] >= 1:
                g.add((Order1, n.HazardousMaterialCategoryNameCode, Literal(HAN[2][0])))
                if HANComponents[2] >= 2:
                    g.add((Order1, n.CodeListIdentificationCode, Literal(HAN[2][1])))
                    if HANComponents[2] >= 3:
                        g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(HAN[2][2])))
                        if HANComponents[2] >= 4:
                            g.add((Order1, n.HazardousMaterialCategoryName, Literal(HAN[2][3])))

        # STG
        if STGElements >= 2:
            g.add((Order1, n.ProcessStageCodeQualifier, Literal(STG[1][0])))
        if STGElements >= 3:
            g.add((Order1, n.ProcessStagesQuantity, Literal(STG[2][0])))
        if STGElements >= 4:
            g.add((Order1, n.ProcessStagesActualQuantity, Literal(STG[3][0])))

        #EFI
        if EFIElements >= 2:
            g.add((Order1, n.FileName, Literal(EFI[1][0])))
            if EFIComponents[1] >= 2:
                g.add((Order1, n.ItemDescription, Literal(EFI[1][1])))
        if EFIElements >= 3:
            g.add((Order1, n.FileFormatName, Literal(EFI[2][0])))
            if EFIComponents[2] >= 2:
                g.add((Order1, n.VersionIdentifier, Literal(EFI[2][1])))
                if EFIComponents[2] >= 3:
                    g.add((Order1, n.DataFormatDescriptionCode, Literal(EFI[2][2])))
                    if EFIComponents[2] >= 4:
                        g.add((Order1, n.DataFormatDescription, Literal(EFI[2][3])))
        if EFIElements >= 4:
            g.add((Order1, n.SequencePositionIdentifier, Literal(EFI[3][0])))
        if EFIElements >= 5:
            g.add((Order1, n.FileCompressionTechniqueName, Literal(EFI[4][0])))

        #CED
        if CEDElements >= 2:
            g.add((Order1, n.ComputerEnvironmentDetailsCodeQualifier, Literal(CED[1][0])))
        if CEDElements >= 3:
            if CEDComponents[2] >= 1:
                g.add((Order1, n.ComputerEnvironmentNameCode, Literal(CED[2][0])))
                if CEDComponents[2] >= 2:
                    g.add((Order1, n.CodeListIdentificationCode, Literal(CED[2][1])))
                    if CEDComponents[2] >= 3:
                        g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(CED[2][2])))
                        if CEDComponents[2] >= 4:
                            g.add((Order1, n.ComputerEnvironmentName, Literal(CED[2][3])))
                            if CEDComponents[2] >= 5:
                                g.add((Order1, n.VersionIdentifier, Literal(CED[2][4])))
                                if CEDComponents[2] >= 6:
                                    g.add((Order1, n.ReleaseIdentifier, Literal(CED[2][5])))
                                    if CEDComponents[2] >= 7:
                                        g.add((Order1, n.ObjectIdentifier, Literal(CED[2][6])))
        if CEDElements >= 4:
            g.add((Order1, n.FileGenerationCommandName, Literal(CED[3][0])))

        #STS
        if STSElements >= 2:
            g.add((Order1, n.StatusCategoryCode, Literal(STS[1][0])))
            if STSComponents[1] >= 2:
                g.add((Order1, n.CodeListIdentificationCode, Literal(STS[1][1])))
                if STSComponents[1] >= 3:
                    g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(STS[1][2])))
        if STSElements >= 3:
            if STSComponents[2] >= 1:
                g.add((Order1, n.StatusDescriptionCode, Literal(STS[2][0])))
                if STSComponents[2] >= 2:
                    g.add((Order1, n.CodeListIdentificationCode, Literal(STS[2][1])))
                    if STSComponents[2] >= 3:
                        g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(STS[2][2])))
                        if STSComponents[2] >= 4:
                            g.add((Order1, n.StatusDescription, Literal(STS[2][3])))
        if STSElements >= 4:
            if STSComponents[3] >= 1:
                g.add((Order1, n.StatusReasonDescriptionCode, Literal(STS[3][0])))
                if STSComponents[3] >= 2:
                    g.add((Order1, n.CodeListIdentificationCode, Literal(STS[3][1])))
                    if STSComponents[3] >= 3:
                        g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(STS[3][2])))
                        if STSComponents[3] >= 4:
                            g.add((Order1, n.StatusReasonDescription, Literal(STS[3][3])))
        if STSElements >= 5:
            if STSComponents[4] >= 1:
                g.add((Order1, n.StatusReasonDescriptionCode, Literal(STS[4][0])))
                if STSComponents[4] >= 2:
                    g.add((Order1, n.CodeListIdentificationCode, Literal(STS[4][1])))
                    if STSComponents[4] >= 3:
                        g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(STS[4][2])))
                        if STSComponents[4] >= 4:
                            g.add((Order1, n.StatusReasonDescription, Literal(STS[4][3])))
        if STSElements >= 6:
            if STSComponents[5] >= 1:
                g.add((Order1, n.StatusReasonDescriptionCode, Literal(STS[5][0])))
                if STSComponents[5] >= 2:
                    g.add((Order1, n.CodeListIdentificationCode, Literal(STS[5][1])))
                    if STSComponents[5] >= 3:
                        g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(STS[5][2])))
                        if STSComponents[5] >= 4:
                            g.add((Order1, n.StatusReasonDescription, Literal(STS[5][3])))
        if STSElements >= 7:
            if STSComponents[6] >= 1:
                g.add((Order1, n.StatusReasonDescriptionCode, Literal(STS[6][0])))
                if STSComponents[6] >= 2:
                    g.add((Order1, n.CodeListIdentificationCode, Literal(STS[6][1])))
                    if STSComponents[6] >= 3:
                        g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(STS[6][2])))
                        if STSComponents[6] >= 4:
                            g.add((Order1, n.StatusReasonDescription, Literal(STS[6][3])))
        if STSElements >= 8:
            if STSComponents[7] >= 1:
                g.add((Order1, n.StatusReasonDescriptionCode, Literal(STS[7][0])))
                if STSComponents[7] >= 2:
                    g.add((Order1, n.CodeListIdentificationCode, Literal(STS[7][1])))
                    if STSComponents[7] >= 3:
                        g.add((Order1, n.CodeListResponsibleAgencyCode, Literal(STS[7][2])))
                        if STSComponents[7] >= 4:
                            g.add((Order1, n.StatusReasonDescription, Literal(STS[7][3])))

                                            # Add triples using store's add method.


# Iterate over triples in store and print them out.
import sys

sys.stdout = open('outputfile1.ttl', 'w')


# For each foaf:Person in the store print out its mbox property.
for person in g.subjects(RDF.type, FOAF.Person):
  for mbox in g.objects(person, FOAF.mbox):
    print(mbox)

# Bind a few prefix, namespace pairs for more readable output
g.bind("dc", DC)
g.bind("foaf", FOAF)





print( g.serialize(format='n3') )

