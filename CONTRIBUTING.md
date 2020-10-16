[This blog post](https://blog.seemsgood.com/how-my-r-houston-headline-bot-works/) explains how the bot works.

In short, add the domain and a regex that will catch the headline to `hhb_regexes.py` .

Be sure to account for the possibility that a headline could contain a quotation mark (`"`).

# What sites should I add to the bot?

Top domains not recognized by the bot, as reported by the bot (does not include domains that the bot obviously isn't useful for), with the 5 most recent examples (as of 2020-10-15)

Feel free to create an issue for any of these domains so that you may then mark that issue as solved.

* www.texasmonthly.com
* * https://redd.it/gygeoz
* * https://redd.it/gws217
* * https://redd.it/gupe6f
* * https://redd.it/gl1d02
* * https://redd.it/gdjxki
* www.fox26houston.com
* * https://redd.it/gmvjol
* * https://redd.it/g91uxp
* * https://redd.it/g7cwus
* * https://redd.it/g1zt47
* * https://redd.it/fxf34m
* houston.culturemap.com
* * https://redd.it/gv6eiu
* * https://redd.it/grlxfc
* * https://redd.it/gmsbsc
* * https://redd.it/gm3cs2
* * https://redd.it/gg3nd1
* www.houstoniamag.com
* * https://redd.it/gyzdwd
* * https://redd.it/gwg8gl
* * https://redd.it/grmgpi
* * https://redd.it/gqvswy
* * https://redd.it/g6lku8
* preview.houstonchronicle.com
* * https://redd.it/gwogav
* * https://redd.it/gwkdc3
* * https://redd.it/go04x8
* * https://redd.it/gjdjmw
* * https://redd.it/fwa4o5
* www.houstononthecheap.com
* * https://redd.it/gorss0
* * https://redd.it/gmuvcb
* * https://redd.it/gj6175
* * https://redd.it/g1a4bv
* * https://redd.it/fxhwq5
* houston.eater.com
* * https://redd.it/gsug6t
* * https://redd.it/gdxpcf
* * https://redd.it/gdj3r4
* * https://redd.it/ga0zzh
* * https://redd.it/g63b61
* www.houstonpress.com
* * https://redd.it/gvv9te
* * https://redd.it/gufcvn
* * https://redd.it/goblcf
* * https://redd.it/gb1pap
* * https://redd.it/g5nezq
* communityimpact.com
* * https://redd.it/gxqg02
* * https://redd.it/gdmxw3
* * https://redd.it/g71oac
* * https://redd.it/fxshkt
* * https://redd.it/fak8j5
* www.texastribune.org
* * https://redd.it/gx2xkx
* * https://redd.it/gw7021
* * https://redd.it/grmy5s
* * https://redd.it/g6y5l2
* * https://redd.it/fhopsi

# Other thoughts

After contributing, I'll want to do _some_ kinda commit to make sure that the post-commit hook gets called. This may simply take the form of updating the above list.