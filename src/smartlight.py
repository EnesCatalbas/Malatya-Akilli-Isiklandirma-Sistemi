import traci
import sumolib

sumoBinary = sumolib.checkBinary('sumo-gui')
traci.start([sumoBinary,"-c", "osm.sumocfg"])

LIGHT_ID_THIS = "12584873252"       
DETECTOR_ID_THIS = "e2_5"           
DETECTOR_ID_NEXT = "e2_2"           

THRESHOLD = 3                       
GREEN_EXTEND = 10                   

print("Simülasyon başladı...")
print("Dedektörler:", traci.lanearea.getIDList())
print("Işıklar:", traci.trafficlight.getIDList())

step = 0
while step < 2000:
    traci.simulationStep()

    if DETECTOR_ID_THIS in traci.lanearea.getIDList():
        veh_this = traci.lanearea.getLastStepVehicleNumber(DETECTOR_ID_THIS)
    else:
        print(f"Dedektör bulunamadı: {DETECTOR_ID_THIS}")
        break

    if DETECTOR_ID_NEXT in traci.lanearea.getIDList():
        veh_next = traci.lanearea.getLastStepVehicleNumber(DETECTOR_ID_NEXT)
    else:
        veh_next = 0 
        print(f"Sonraki dedektör bulunamadı: {DETECTOR_ID_NEXT}")

    if LIGHT_ID_THIS in traci.trafficlight.getIDList():
        current_phase = traci.trafficlight.getPhase(LIGHT_ID_THIS)
        remaining = traci.trafficlight.getNextSwitch(LIGHT_ID_THIS) - traci.simulation.getTime()
    else:
        print(f"Trafik ışığı bulunamadı: {LIGHT_ID_THIS}")
        break

    if veh_next < (veh_this / 1.5):
        print(f"{step}: {LIGHT_ID_THIS} - Bu kavşakta {veh_this}, sonraki {veh_next}. "
              f"Yeşil {GREEN_EXTEND}s uzatıldı.")
        traci.trafficlight.setPhaseDuration(LIGHT_ID_THIS, GREEN_EXTEND)

    step += 1

print("Simülasyon bitti.")
traci.close()

