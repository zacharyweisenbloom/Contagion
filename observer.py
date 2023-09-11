"""Generic Observer (aka Listener) mechanics (abstract base classes) for
connecting any Observable object (e.g., a view) to one or more Observer objects 
(e.g., a controller or a model).

Also included in this module are to example concrete implementations:
    - a concrete class, Watcher, which extends Observer and is used to monitor 
    changes in other classes to which it is attached.
    - a concrete class, Watched, which extends Observable and shows how to
    attach an Observer to it, so it would be notified whenever the Watched 
    instances change.
"""

from typing import List

###############################################################################
# Interface definitions (abstract base classes) for the Observer and Observable
###############################################################################

class Observer:
    """Interface that should be implemented by classes that wish to be notified
    when certain events (in other classes) occur.
    
    For example, in MVC, a controller might be notified when the model changes, 
    and the controller might be notified when the view changes.
    """
    def receive_notification(self, subject: "Observable", event: str):
        """Notify the observer that the subject has changed.
        
        Args:
            subject: the Observable object that has changed
            event: the event that occurred
        """
        raise NotImplementedError("The 'Observer.notify' method MUST" 
                                  "be defined in concrete classes")

class Observable:
    """Interface that should be implemented by classes that wish to 
    notify other objects when certain changes in their own state occur.
    
    For example, in MVC, a view can be monitored (observed) by a controller
    whenever the user provides input into the view.
    """

    def __init__(self):
        self._observers: List[Observer] = []

    def add_observer(self, observer: Observer):
        self._observers.append(observer)

    def notify_all(self, event: str):
        for observer in self._observers:
            observer.receive_notification(self, event)   # implemented by Observer subclasses
            
            
###############################################################################
# Concrete classes (examples)
###############################################################################
# Example concrete implementation of Observer
class Watcher(Observer):
    """Implements the Observer interface. This is a concrete class that 
    can be instantiated and used normally.
    """
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    def receive_notification(self, subject: "Observable", event: str):
        print(f"{self.name} is watching {subject} and heard that {event}")
        
        
# Example concrete implementation of Observable
class Watched(Observable):
    """Implements the Observable interface. This is a concrete class that 
    can be instantiated and used normally.
    """
    def __init__(self, name: str):
        super().__init__()
        self.name = name
        self.thingy = False
        
    def __str__(self):
        return self.name
    
    def do_something(self):
        self.thingy = not self.thingy   # change the state of self
        self.notify_all(f"{self.name} is doing something silly")    
    
    
def main():
    # Smoke test: instantiate Watched and Watcher, and attach them to each other

    nosy_neigbor = Watcher("Nosy Neighbor")
    
    kate = Watched("Kate")
    kate.add_observer(nosy_neigbor)
    
    bob = Watched("Bob")
    bob.add_observer(nosy_neigbor)
    
    # Do stuff, the following two statements
    kate.do_something()
    bob.do_something()
    # should print something like:
    # Nosy Neighbor is watching Kate and heard that Kate is doing something silly
    # Nosy Neighbor is watching Bob and heard that Bob is doing something silly
    
    
if __name__ == "__main__":
    main()
    
    