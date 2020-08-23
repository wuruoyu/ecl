#!/usr/bin/python3
import sys
import os
import getopt
from subprocess import call

ECL_DIR = "/home/ruoyu/workspace/numeric/ecl/"
PASS_DIR = "/home/ruoyu/workspace/numeric/pass/"
SYMCC_DIR = "/home/ruoyu/workspace/numeric/symcc/"

def main(argv):

    test_option = sys.argv[1]

    os.chdir(ECL_DIR)

    if test_option == 'normal':
        os.environ['CC'] = "clang"
        os.environ['CXX'] = "clang++"
        MAIN_CXX = "clang++"
    elif test_option == 'numeric':
        os.environ['CC'] = PASS_DIR + "numeric"
        os.environ['CXX'] = PASS_DIR + "numeric++"
        MAIN_CXX = PASS_DIR + "numeric++_main"
    elif test_option == 'numeric_symcc':
        os.environ['CC'] = SYMCC_DIR + "symcc_numeric"
        os.environ['CXX'] = SYMCC_DIR + "sym++_numeric"
        os.environ['SYMCC_INPUT_FILE'] = PASS_DIR + "test/replay_sensor/sample_sensor_data.txt"
        MAIN_CXX = SYMCC_DIR + "sym++_numeric_main"
    else:
        print("error")
    
    call("make clean", shell=True)
    call("make test -n > ./compile_test.log", shell=True)
    call("trash bin/" + test_option + "_ekf_replay", shell=True)

    call(MAIN_CXX + " -DECL_STANDALONE -I./build/test_build/matrix-prefix/src/matrix -I../../ -I. -g -std=gnu++14 -o build/test_build/test/CMakeFiles/ECL_GTESTS.dir/test_EKF_replay_sym.cpp.o -c /home/ruoyu/workspace/numeric/ecl/test/test_EKF_replay_sym.cpp", shell=True)

    call(MAIN_CXX + " -g -rdynamic build/test_build/test/CMakeFiles/ECL_GTESTS.dir/test_EKF_replay_sym.cpp.o build/test_build/EKF/libecl_EKF.a build/test_build/test/sensor_simulator/libecl_sensor_sim.a build/test_build/test/test_helper/libecl_test_helper.a -lpthread build/test_build/EKF/libecl_EKF.a build/test_build/geo/libecl_geo.a build/test_build/geo_lookup/libecl_geo_lookup.a -o bin/" + test_option + "_ekf_replay", shell=True)


if __name__ == "__main__":
    main(sys.argv[1:])

    
