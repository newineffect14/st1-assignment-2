Before using AI i used the human code from the lab doc to test run. However i found many issues and limitations including no recognition of clashed appointments, no checking empty practioner name, and no way to cancel appointments

Using AI as a tutor helped me to realise why raising ValueError is better than silently ignoring the bad input .

When I asked AI to generate an alternative version, it made the assumption that patient_name would always be valid / no duplicate checking was needed and these were assumptions I only caught once I tested it with a blank input and it didn't raise an error.

I verified the AI output by running both versions against the four test cases from Part F and comparing what happened when the AI version silently accepted a blank name while my version raised an error for example.

The engineering work that remained mine was deciding which single improvement to actually apply in Part G, and why, along with judging which version's error-handling behaviour was actually correct for a clinic booking system. 