# FangBot
### Configuration
1. Remove the .sample extensions from the following files:
- .env.sample
- roles.csv.sample
- snoot.txt.sample
- nuggie.txt.sample
- tail.txt.sample
- oracle.txt.sample
2. Replace the placeholder values in .env with your bot's token, the various IDs for objects, and the limit on pings/emoji in a single post. To grab IDs: enable developer mode in Discord advanced settings, right click on the relevant object, and select "Copy objectname ID".
3. Populate the roles.csv file with the roles you want the bot to grant whenever a user reacts to the welcome post. Syntax should be: emojiname,role ID. The file should be UTF-8 encoded.
4. Populate the snoot.txt, tail.txt, oracle.txt and nuggie.txt files with the responses you want the bot to use when those commands are invoked. Emoji should be in the format: <:emojiname:emojiID>. Ie: <:reedstare:870688770545033216>. For the tail command specifically, the first line used will be 1-in-1000 response for some lucky user.
