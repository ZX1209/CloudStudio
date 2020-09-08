If you want to access virtual memory of a specific process: refer to @Stéphane's answer.

If you want to access physical memory:

If you have devmem installed:

devmem 0x2000000 
Alternative approach with hexdump:

hexdump -C --skip 0x7fffffffeb58 /dev/mem | head
See this question on StackOverflow.