# Raffle

Thanks to our [community sponsors](https://boyaconf.com/#sponsors) we have some prizes to raffle, so we have created a script that will pick random people as winners.

## How does it work?

The selection process is as follows:
1. Read the whole list of attendees (we don't include organizers, staff, speakers or sponsors) and pick only those that were registered at event's opening.
2. Shuffle that list.
3. Pick `p` random numbers from 0 to `n`, where `p` is the number of prizes and `n` is the number of attendees picked in step 1.
4. Create a list by picking attendees at index `w` where `w` is each one of the numbers picked in step 3.
5. Shuffle the "pre-winners" list.
6. Assign each prize a winner from the result list in step 5.