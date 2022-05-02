#include "thread_coord.h"

#include <fstream>

using namespace std;

ThreadCoord thread_coord;
ofstream debug_fout(thread_coord.filename);
