# List all script files to be processed
SCRIPTS = 0-RSA_public_key.pub 1-for_best_school 2-while_best_school 3-until_best_school \
          4-if_9_say_hi 5-4_bad_luck_8_is_your_chance 6-superstitious_numbers 7-clock \
          8-for_ls 9-to_file_or_not_to_file 10-fizzbuzz 100-read_and_cut \
          101-tell_the_story_of_passwd 102-lets_parse_apache_logs 103-dig_the-data

# Target to make all scripts executable
all: make_executable test_scripts

# Make scripts executable
make_executable:
	@echo "Making scripts executable..."
	@for script in $(SCRIPTS); do \
		chmod +x $$script; \
	done
	@echo "All scripts are now executable."

# Test each script
test_scripts:
	@echo "Testing scripts..."
	@for script in $(SCRIPTS); do \
		echo "Running $$script..."; \
		./$$script || echo "$$script failed"; \
	done
	@echo "All tests completed."

# Clean target for resetting permissions (optional)
clean:
	@echo "Removing executable permissions..."
	@for script in $(SCRIPTS); do \
		chmod -x $$script; \
	done
	@echo "Permissions reset."
