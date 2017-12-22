# ThreadPool is a simple thread pool
#
# Copyright (C) 2012 Yummy Bian <yummy.bian#gmail.com>
#
# under the terms of the GNU Lesser General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ThreadPool is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.";
#

import sys
import Queue
import threading
import time
import traceback

class Worker(threading.Thread):
    """Routines for work thread."""

    def __init__(self, in_queue, out_queue, err_queue):
        """Initialize and launch a work thread,
        in_queue which tasks in it waiting for processing,
        out_queue which the return value of the task in it,
        err_queue which stores error info when processing the task.
        """
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.in_queue = in_queue
        self.out_queue = out_queue
        self.err_queue = err_queue
        self.start()

    def run(self):
        while True:
            # Processing tasks in the in_queue until command is stop.
            command, callback, args, kwds = self.in_queue.get()
            if command == 'stop':
                break
            if command == 'process':
                try:
                    self.out_queue.put(callback(*args, **kwds))
                except Exception:
                    pass
            else:
                time.sleep(0.1)
           
    def dismiss(self):
        command = 'stop'
        self.in_queue.put((command, None, None, None))

    def report_error(self):
        '''We "report" errors by adding error information to err_queue.'''
        self.err_queue.put(sys.exc_info()[:2])


class ThreadPool():
    """Manager thread pool."""
    max_threads = 32

    def __init__(self, num_threads, pool_size=0):
        """Spawn num_threads threads in the thread pool,
        and initialize three queues.
        """
        # pool_size = 0 indicates buffer is unlimited.
        self.num_threads = ThreadPool.max_threads \
            if num_threads > ThreadPool.max_threads \
            else num_threads
        self.in_queue = Queue.Queue(pool_size)
        self.out_queue = Queue.Queue(pool_size)
        self.err_queue = Queue.Queue(pool_size)
        self.workers = {}
        for i in range(self.num_threads):
            worker = Worker(self.in_queue, self.out_queue, self.err_queue)
            self.workers[i] = worker
        self.is_continue = True

    def add_task(self, callback, *args, **kwds):
        command = 'process'
        self.in_queue.put((command, callback, args, kwds))

    def _get_results(self, queue):
        '''Generator to yield one after the others all items currently
           in the queue, without any waiting
        '''
        try:
            while True:
                yield queue.get_nowait()
        except Queue.Empty:
            raise StopIteration

    def get_task(self):
        return self.out_queue.get()

    def wait(self):
        _is = False
        for i in range(self.num_threads):
            if self.workers[i].is_alive():
                _is = True
                break
        return _is
        

    def show_results(self):
        for result in self._get_results(self.out_queue):
            print 'Result:', result

    def show_errors(self):
        for etyp, err in self._get_results(self.err_queue):
            print 'Error:', etyp, err

    def destroy(self):
        # order is important: first, request all threads to stop...:
        for i in self.workers:
            self.workers[i].dismiss()
        # ...then, wait for each of them to terminate:
        for i in self.workers:
            self.workers[i].join()
        # clean up the workers from now-unused thread objects
        del self.workers

