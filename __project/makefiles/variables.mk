# Print the variables as they are known to make.
show_vars:
	@$(foreach \
	     var,$(sort $(.VARIABLES)), \
		 $(if \
		     $(filter-out environment% default automatic, $(origin $(var))), \
		     echo "$(var)=$($(var))"; \
		 ))