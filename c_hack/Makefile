PROJECTS = $(shell ls ./)
clean:
	@echo "Projects: $(PROJECTS)"
	@for prj in $(PROJECTS);	\
	do make -C $${prj}/ clean;	\
	done

.PHONY : clean
