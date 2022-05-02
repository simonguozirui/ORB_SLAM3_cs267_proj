#ifndef THREAD_COORD_H
#define THREAD_COORD_H

#include <thread>
#include <vector>
#include <fstream>
#include "../core/solver.h"

struct ThreadCoord {
    std::thread::id local_mapping_id;
    int omp_num_threads = 2;
    double t_loop1 = 0, t_loop2 = 0, t_loop3 = 0;
    double t_schur_load = 0;
    std::vector<double> t_overhead;
    std::vector<double> t_loop3_init;
    std::vector<double> t_mult;
    std::vector<double> t_sub;
    std::vector<double> t_load;
    std::vector<double> t_store;
    std::vector<double> count;
    bool is_full_inertial_ba = false;
    bool is_local_ba = false;
    bool is_inertial_opt = false;

    std::string filename = "/app/data/omp_" + std::to_string(omp_num_threads) + "_load.csv";
};

#endif // THREAD_COORD_H
