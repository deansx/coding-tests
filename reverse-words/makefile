# makefile for the sim_exec test

# compiler args:
CC=g++
CVERS=-std=c++11
LDFLAGS=-g
TESTS=-DFXN_TST -DTEST_HARNESS -DMSG_VERBOSE
DEFS=$(TESTS) -DLINUX
#WARNS=-Wno-deprecated -Wno-write-strings 
CFLAGS=$(CVERS) $(WARNS) $(DEFS) $(LDFLAGS)

# directories
UTIL=../utils/
RWRD=../reverse-words/

INCLUDES=-I . -I $(RWRD) -I $(UTIL)

SOURCES=$(RWRD)reverse-words.cc

OBJECTS=$(SOURCES:.cc=.o)
EXECUTABLE=reverse-words

all: $(SOURCES) $(EXECUTABLE)
$(EXECUTABLE): $(OBJECTS)
	$(CC) $(LDFLAGS) $(OBJECTS) -o $@

# $(call make-depend,source-file,object-file,depend-file)
define make-depend
  $(CC) -MM -MF $3 -MP -MT $2 $(INCLUDES) $(CFLAGS) $1
endef

%.o: %.cc
	$(call make-depend,$<,$@,$(subst .o,.d,$@))
	$(CC) $(INCLUDES) $(CFLAGS) -c $< -o $@

ifneq "$(MAKECMDGOALS)" "clean"
  -include $(subst .cc,.d,$(SOURCES))
endif

clean:
	rm -vf $(OBJECTS)
	rm -vf $(EXECUTABLE).exe
	rm -vf $(subst .cc,.d,$(SOURCES))
