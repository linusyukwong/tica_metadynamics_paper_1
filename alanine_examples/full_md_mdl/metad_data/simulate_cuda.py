import os
from simtk.openmm.app import *
from simtk.openmm import *
from simtk.unit import *
from sys import stdout
import optparse
import shutil
import warnings
from IPython import embed
from msmbuilder.io import backup
#import openmmplumed
#from openmmplumed import PlumedForce
from plumed import plumed_script

def serializeObject(obj,objname):
    objfile = open(objname,'w')
    objfile.write(XmlSerializer.serialize(obj))
    objfile.close()


def continue_running():
  print(plumed_script)
  if os.path.isfile("./state_cuda.xml"):
    state = XmlSerializer.deserialize(open("./state_cuda.xml").read())
  else:
    state = XmlSerializer.deserialize(open("../../starting_coordinates/state.xml").read())
  
  
  system =  XmlSerializer.deserialize(open("../../starting_coordinates/system.xml").read())

  integrator = XmlSerializer.deserialize(open("../../starting_coordinates/integrator.xml").read())

  pdb = app.PDBFile("../../starting_coordinates/0.pdb")


  #system.addForce(PlumedForce(plumed_script))
  print("here")
  platform = Platform.getPlatformByName("CUDA")
  properties = {'CudaPrecision': 'mixed'}
  simulation = app.Simulation(pdb.topology, system, integrator, platform, properties)
  simulation.context.setState(state)

  backup("trajectory_cuda.dcd")
  f = open("./speed_report_cuda.txt",'w')
  simulation.reporters.append(app.DCDReporter('trajectory_cuda.dcd', 5000))
  simulation.reporters.append(app.StateDataReporter(f, 5000, step=True,\
                                potentialEnergy=True, temperature=True, progress=True, remainingTime=True,\
                                speed=True, totalSteps=17269*5000, separator='\t'))

  #run for 23hrs
  #simulation.runForClockTime(3,stateFile="state.xml")
  simulation.step(17269*5000)
  backup("state_cuda.xml")
  state=simulation.context.getState(getPositions=True, getVelocities=True,\
    getForces=True,getEnergy=True,getParameters=True,enforcePeriodicBox=True)
  serializeObject(state,'state_cuda.xml')

if __name__=="__main__":
    continue_running()
