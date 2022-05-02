#ifndef THREAD_COORD_H
#define THREAD_COORD_H

#include <thread>


struct ThreadCoord {
    std::thread::id local_mapping_id;
    std::thread::id loop_closure_id;
    std::thread::id tracking_id;
    bool is_local_ba = false;
};

#endif