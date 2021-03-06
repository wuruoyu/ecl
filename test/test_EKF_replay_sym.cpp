#include <math.h>
#include <memory>
#include <iostream>
#include "../EKF/ekf.h"
#include "sensor_simulator/sensor_simulator.h"
#include "sensor_simulator/ekf_wrapper.h"
#include "sensor_simulator/ekf_logger.h"

int main()
{
  auto _ekf = std::make_shared<Ekf>();

  SensorSimulator _sensor_simulator(_ekf);

  EkfWrapper _ekf_wrapper(_ekf);
  EkfLogger _ekf_logger(_ekf);

  _sensor_simulator.loadSensorDataFromFileSym("/home/ruoyu/workspace/numeric/pass/test/replay_sensor/sample_sensor_data.txt");

  //_ekf_logger.setFilePath("/home/wuruoyu/workspace/numeric/lib/ecl/test/change_indication/iris_gps.csv");

  // Start simulation and enable fusion of additional sensor types here
  // By default the IMU, Baro and Mag sensor simulators are already running
  
  // TODO: enable the GPS
  //_sensor_simulator.startGps();
  //_ekf_wrapper.enableGpsFusion();

  uint8_t logging_rate_hz = 100;
  for(int i = 0; i < 9 * logging_rate_hz; ++i)
  {
    std::cout << "each step" << std::endl;
    _sensor_simulator.runReplaySeconds(1.0f / logging_rate_hz);
    //_ekf_logger.writeStateToFile();
  }
}

