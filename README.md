# wordle_subtle_helper
This tool shows how many words satisfy the clues in the current wordle puzzle at each step and lists the possible words if the user wants

An example run for day 260:


murataslan@Murats-MacBook-Air subtle_helper % python3 helper_v2.py

2315

Enter guess 1: brake

Enter colors of guess 1: (Not in word = 0, Green = G, Yellow = Y) 00000

Do you confirm, Y/N or press B to go back 1 step Y

There are 373 possible words, do you want to show them? Y/N Y

['child\n', 'chili\n', 'chill\n', 'chump\n', 'cinch\n', 'civic\n', 'civil\n', 'cliff\n', 'cling\n', 'cloth\n', 'cloud\n', 'clout\n', 'clown\n', 'clump\n', 'clung\n', 'colon\n', 'comfy\n', 'comic\n', 'conch\n', 'condo\n', 'conic\n', 'couch\n', 'cough\n', 'could\n', 'count\n', 'coyly\n', 'cumin\n', 'cynic\n', 'digit\n', 'dilly\n', 'dimly\n', 'dingo\n', 'dingy\n', 'disco\n', 'ditch\n', 'ditto\n', 'ditty\n', 'dizzy\n', 'dodgy\n', 'doing\n', 'dolly\n', 'donut\n', 'dough\n', 'dowdy\n', 'downy\n', 'duchy\n', 'dully\n', 'dummy\n', 'dumpy\n', 'dusty\n', 'dutch\n', 'dying\n', 'ficus\n', 'fifth\n', 'fifty\n', 'fight\n', 'filly\n', 'filmy\n', 'filth\n', 'finch\n', 'fishy\n', 'fizzy\n', 'fling\n', 'flint\n', 'flood\n', 'floss\n', 'flout\n', 'flown\n', 'fluff\n', 'fluid\n', 'flung\n', 'flush\n', 'focus\n', 'foggy\n', 'foist\n', 'folio\n', 'folly\n', 'found\n', 'fully\n', 'fungi\n', 'funny\n', 'fussy\n', 'fuzzy\n', 'ghost\n', 'ghoul\n', 'giddy\n', 'gipsy\n', 'glint\n', 'gloom\n', 'gloss\n', 'glyph\n', 'godly\n', 'going\n', 'golly\n', 'goody\n', 'goofy\n', 'guild\n', 'guilt\n', 'gulch\n', 'gully\n', 'gummy\n', 'guppy\n', 'gusto\n', 'gusty\n', 'gypsy\n', 'hilly\n', 'hippo\n', 'hippy\n', 'hitch\n', 'hoist\n', 'holly\n', 'hotly\n', 'hound\n', 'howdy\n', 'humid\n', 'humph\n', 'humus\n', 'hunch\n', 'hussy\n', 'hutch\n', 'icily\n', 'icing\n', 'idiom\n', 'idiot\n', 'idyll\n', 'igloo\n', 'imply\n', 'ingot\n', 'input\n', 'ionic\n', 'itchy\n', 'jiffy\n', 'joint\n', 'joist\n', 'jolly\n', 'joust\n', 'juicy\n', 'jumpy\n', 'junto\n', 'light\n', 'limit\n', 'lingo\n', 'lipid\n', 'livid\n', 'locus\n', 'lofty\n', 'logic\n', 'login\n', 'loopy\n', 'lousy\n', 'lowly\n', 'lucid\n', 'lumpy\n', 'lunch\n', 'lupus\n', 'lusty\n', 'lying\n', 'lymph\n', 'lynch\n', 'midst\n', 'might\n', 'mimic\n', 'minim\n', 'minty\n', 'minus\n', 'missy\n', 'mogul\n', 'moist\n', 'moldy\n', 'month\n', 'moody\n', 'mossy\n', 'motif\n', 'motto\n', 'moult\n', 'mound\n', 'mount\n', 'mouth\n', 'mucus\n', 'muddy\n', 'mulch\n', 'mummy\n', 'munch\n', 'mushy\n', 'music\n', 'musty\n', 'night\n', 'ninny\n', 'ninth\n', 'noisy\n', 'notch\n', 'nutty\n', 'nylon\n', 'nymph\n', 'oddly\n', 'onion\n', 'opium\n', 'optic\n', 'ought\n', 'outdo\n', 'outgo\n', 'ovoid\n', 'owing\n', 'phony\n', 'photo\n', 'piggy\n', 'pilot\n', 'pinch\n', 'pinto\n', 'pitch\n', 'pithy\n', 'pivot\n', 'plump\n', 'plush\n', 'point\n', 'polyp\n', 'pooch\n', 'poppy\n', 'posit\n', 'pouch\n', 'pound\n', 'pouty\n', 'pudgy\n', 'puffy\n', 'pulpy\n', 'punch\n', 'pupil\n', 'puppy\n', 'pushy\n', 'putty\n', 'pygmy\n', 'quill\n', 'quilt\n', 'quoth\n', 'scion\n', 'scoff\n', 'scold\n', 'scoop\n', 'scout\n', 'scowl\n', 'shift\n', 'shiny\n', 'shoot\n', 'shout\n', 'shown\n', 'showy\n', 'shunt\n', 'shush\n', 'shyly\n', 'sight\n', 'silly\n', 'sissy\n', 'sixth\n', 'sixty\n', 'slimy\n', 'sling\n', 'sloop\n', 'slosh\n', 'sloth\n', 'slump\n', 'slung\n', 'slush\n', 'slyly\n', 'smith\n', 'sniff\n', 'snoop\n', 'snout\n', 'snowy\n', 'snuff\n', 'soggy\n', 'solid\n', 'sonic\n', 'sooth\n', 'sooty\n', 'sound\n', 'south\n', 'spicy\n', 'spill\n', 'spilt\n', 'spiny\n', 'split\n', 'spoil\n', 'spoof\n', 'spool\n', 'spoon\n', 'spout\n', 'stiff\n', 'still\n', 'stilt\n', 'sting\n', 'stint\n', 'stoic\n', 'stomp\n', 'stony\n', 'stood\n', 'stool\n', 'stoop\n', 'stout\n', 'study\n', 'stuff\n', 'stump\n', 'stung\n', 'stunt\n', 'suing\n', 'sully\n', 'sunny\n', 'sushi\n', 'swift\n', 'swill\n', 'swing\n', 'swish\n', 'swoon\n', 'swoop\n', 'swung\n', 'synod\n', 'thigh\n', 'thing\n', 'thong\n', 'thump\n', 'tight\n', 'timid\n', 'tipsy\n', 'toddy\n', 'tonic\n', 'tooth\n', 'topic\n', 'touch\n', 'tough\n', 'toxic\n', 'toxin\n', 'tulip\n', 'tunic\n', 'twist\n', 'twixt\n', 'tying\n', 'uncut\n', 'undid\n', 'unfit\n', 'unify\n', 'union\n', 'unity\n', 'unlit\n', 'until\n', 'unzip\n', 'using\n', 'vigil\n', 'vinyl\n', 'visit\n', 'vivid\n', 'vomit\n', 'vouch\n', 'vying\n', 'which\n', 'whiff\n', 'whiny\n', 'whoop\n', 'widow\n', 'width\n', 'wight\n', 'willy\n', 'wimpy\n', 'winch\n', 'windy\n', 'wispy\n', 'witch\n', 'witty\n', 'woody\n', 'wooly\n', 'woozy\n', 'would\n', 'wound\n', 'young\n', 'youth\n']

Enter guess 2:SLOPY

Enter colors of guess 2: (Not in word = 0, Green = G, Yellow = Y) 0GG00

Do you confirm, Y/N or press B to go back 1 step Y

There are 8 possible words, do you want to show them? Y/N Y

['cloth\n', 'cloud\n', 'clout\n', 'clown\n', 'flood\n', 'flout\n', 'flown\n', 'gloom\n']

Enter guess 3:CLOTH

Enter colors of guess 3: (Not in word = 0, Green = G, Yellow = Y) GGGGG

Do you confirm, Y/N or press B to go back 1 step Y

There are 1 possible words, do you want to show them? Y/N Y

['cloth\n']

murataslan@Murats-MacBook-Air subtle_helper % 
