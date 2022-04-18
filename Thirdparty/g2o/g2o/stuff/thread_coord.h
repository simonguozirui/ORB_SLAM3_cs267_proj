#include <thread>

using namespace std;

struct ThreadCoord {
    std::thread::id local_mapping_id;
};

ThreadCoord thread_coord;
