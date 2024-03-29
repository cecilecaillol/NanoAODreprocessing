# Auto generated configuration file
# using: 
# Revision: 1.19 
# Source: /local/reps/CMSSW/CMSSW/Configuration/Applications/python/ConfigBuilder.py,v 
# with command line options: step1 --no_exec --mc --python_filename run_crab.py --fileout NanoAODv9.root --eventcontent NANOAODSIM --customise Configuration/DataProcessing/Utils.addMonitoring --datatier NANOAODSIM --step NANO -n 6284 --conditions 106X_upgrade2018_realistic_v16_L1v1 --era Run2_2018,run2_nanoAOD_106Xv2
import FWCore.ParameterSet.Config as cms

from Configuration.Eras.Era_Run2_2018_cff import Run2_2018
from Configuration.Eras.Modifier_run2_nanoAOD_106Xv2_cff import run2_nanoAOD_106Xv2

process = cms.Process('NANO',Run2_2018,run2_nanoAOD_106Xv2)

# import of standard configurations
process.load('Configuration.StandardSequences.Services_cff')
process.load('SimGeneral.HepPDTESSource.pythiapdt_cfi')
process.load('FWCore.MessageService.MessageLogger_cfi')
process.load('Configuration.EventContent.EventContent_cff')
process.load('SimGeneral.MixingModule.mixNoPU_cfi')
process.load('Configuration.StandardSequences.GeometryRecoDB_cff')
process.load('Configuration.StandardSequences.MagneticField_cff')
process.load('PhysicsTools.NanoAOD.nano_cff')
process.load('Configuration.StandardSequences.EndOfProcess_cff')
process.load('Configuration.StandardSequences.FrontierConditions_GlobalTag_cff')

process.maxEvents = cms.untracked.PSet(
    input = cms.untracked.int32(-1)
)

# Input source
process.source = cms.Source("PoolSource",
    fileNames = cms.untracked.vstring(
	#'file:/afs/cern.ch/work/c/ccaillol/PrivateMCProduction/EXO-MCsampleProductions/FullSimulation/RunIISummer20UL18/MiniAOD__CMSSW_10_6_20/src/MiniAOD.root'
	#'/store/mc/RunIISummer20UL18MiniAODv2/TTToSemiLeptonic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/120000/006455CD-9CDB-B843-B50D-5721C39F30CE.root',
	#'/store/mc/RunIISummer19UL18MiniAODv2/TTTo2L2Nu_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/240000/000D7BCF-E068-3943-BC04-2C3DDA4824B0.root',
	#'/store/mc/RunIISummer20UL18MiniAODv2/TTToHadronic_TuneCP5_13TeV-powheg-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/00000/62298168-7A8C-D148-B123-9B26E5FB6F88.root',
	#"file:/eos/cms/store/group/phys_smp/Exclusive_DiTau/miniaod/signal/GGToTauTau_M_50GeV_TuneCP5_madgraphLO_reweight/GGToTauTau_M_50GeV_TuneCP5_madgraphLO_reweight_0021.root",
	#'/store/mc/RunIISummer20UL18MiniAODv2/WJetsToLNu_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v1/00000/0E3C9275-BEFE-E749-A5C1-7097933F8338.root'
	#'/store/mc/RunIISummer20UL18MiniAODv2/DYJetsToLL_M-50_TuneCP5_13TeV-madgraphMLM-pythia8/MINIAODSIM/106X_upgrade2018_realistic_v16_L1v1-v2/120000/001C8DDF-599C-5E45-BF2C-76F887C9ADE9.root'
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0950.root',
        ##'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0951.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0952.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0953.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0954.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0955.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0956.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0957.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0958.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0959.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0960.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0961.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0962.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0963.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0964.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0965.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0966.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0967.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0968.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0969.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0970.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0971.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0972.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0973.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0974.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0975.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0976.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0977.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0978.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0979.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0980.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0981.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0982.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0983.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0984.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0985.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0986.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0987.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0988.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0989.root',
	#'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0990.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0991.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0992.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0993.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0994.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0995.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0996.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0997.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0998.root',
        #'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToWW_dilep_Elastic_Mll_50GeV_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToWW_Elastic_M_50GeV_PTFilter_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0999.root'
	 'file:/eos/cms/store/cmst3/group/taug2/MiniAOD/GGToTauTau_Elastic_M_50GeV_PTFilter_ktSmear_RunIISummer20UL18_TuneCP5_madgraphLO_reweight/GGToTauTau_Elastic_M_50GeV_PTFilter_ktSmear_RunIISummer20UL18_TuneCP5_madgraphLO_reweight_0431.root'
    ),
    secondaryFileNames = cms.untracked.vstring()
)

process.source.duplicateCheckMode = cms.untracked.string('noDuplicateCheck')

process.options = cms.untracked.PSet(

)

# Production Info
process.configurationMetadata = cms.untracked.PSet(
    annotation = cms.untracked.string('step1 nevts:6284'),
    name = cms.untracked.string('Applications'),
    version = cms.untracked.string('$Revision: 1.19 $')
)

# Output definition

process.NANOAODSIMoutput = cms.OutputModule("NanoAODOutputModule",
    compressionAlgorithm = cms.untracked.string('LZMA'),
    compressionLevel = cms.untracked.int32(9),
    dataset = cms.untracked.PSet(
        dataTier = cms.untracked.string('NANOAODSIM'),
        filterName = cms.untracked.string('')
    ),
    fileName = cms.untracked.string('NanoAODv9.root'),
    SelectEvents = cms.untracked.PSet(
      SelectEvents = cms.vstring('nanoAOD_step')
    ),
    outputCommands = process.NANOAODSIMEventContent.outputCommands
)

# Additional output definition

# Other statements
from Configuration.AlCa.GlobalTag import GlobalTag
process.GlobalTag = GlobalTag(process.GlobalTag, '106X_upgrade2018_realistic_v16_L1v1', '')

# Path and EndPath definitions

process.ditauFilter = cms.EDFilter("DiTauFilter",
     electrons   = cms.InputTag("slimmedElectrons"),
     muons       = cms.InputTag("slimmedMuons"),
     taus        = cms.InputTag("slimmedTaus")
   )

process.nanoAOD_selection = cms.Sequence(process.ditauFilter)

process.lheWeightsTable = cms.EDProducer(
    "ReweightingProducer",
    lheInfo = cms.VInputTag(cms.InputTag("externalLHEProducer"), cms.InputTag("source"))
)

process.nanoAOD_step = cms.Path(process.nanoAOD_selection * process.nanoSequenceMC)
process.nanoAOD_step += process.lheWeightsTable
process.endjob_step = cms.EndPath(process.endOfProcess)
process.NANOAODSIMoutput_step = cms.EndPath(process.NANOAODSIMoutput)

# Schedule definition
process.schedule = cms.Schedule(process.nanoAOD_step,process.endjob_step,process.NANOAODSIMoutput_step)
from PhysicsTools.PatAlgos.tools.helpers import associatePatAlgosToolsTask
associatePatAlgosToolsTask(process)

# customisation of the process.

# Automatic addition of the customisation function from PhysicsTools.NanoAOD.nano_cff
from PhysicsTools.NanoAOD.nano_cff import nanoAOD_customizeMC 

#call to customisation function nanoAOD_customizeMC imported from PhysicsTools.NanoAOD.nano_cff
process = nanoAOD_customizeMC(process)

# Automatic addition of the customisation function from Configuration.DataProcessing.Utils
from Configuration.DataProcessing.Utils import addMonitoring 

#call to customisation function addMonitoring imported from Configuration.DataProcessing.Utils
process = addMonitoring(process)

# End of customisation functions

# Customisation from command line

# Add early deletion of temporary data products to reduce peak memory need
from Configuration.StandardSequences.earlyDeleteSettings_cff import customiseEarlyDelete
process = customiseEarlyDelete(process)
# End adding early deletion
