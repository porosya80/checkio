#!/home/porosya/.local/share/virtualenvs/checkio-VEsvC6M1/bin/checkio --domain=py run crossword-solver

# https://py.checkio.org/mission/crossword-solver/

# “Looking at the sky, he suddenly saw that it had become black. Then white again, but with great rippling        circles. The circles were vultures wheeling around the sun. The vultures disappeared, to be replaced by checkers        squares ready to be played on. On the board, the pieces moved around incredibly rapidly, winning dozens of games        every minute. They were scarcely lined up before they started rushing at each other again, banging into each        other, forming fighting combinations, wiping the other side out in the wink of an eye. Then the squares        scattered, giving way to the grille of a crossword puzzle, and here, too, words flashed, drove each other away,        clustered, were erased. They were all very long words, like Catalepsy, Thunderbird, Superrequeteriquísímo and        Anticonstitutionally.”
# ― Jean-Marie G. Le Clézio, The Book of Flights
# 
# Acrosswordis a word puzzle that normally takes the form of a square or a rectangular grid of white and black    shaded squares. The goal is to fill the white squares with letters, forming words or phrases, by solving clues which    lead to the answers. In languages that are written left-to-right, the answer words and phrases are placed in the    grid from left to right and from top to bottom. The shaded squares are used to separate the words or phrases.
# 
# We will solve a few crosswords which have a lattice-like structure,    with a higher percentage of shaded squares, leaving up to half the letters in an answer unchecked.    For example, if the top row has an answer running all the way across,    there will be no across answers in the second row.    Your program receives a crossword pattern without clues and numbers, and it should determine word positions itself    with    the following rules:
# - If a cell is placed in the most left column or neighbour left cell is shaded, and the neighbouring right cell is    empty, then this cell is the beginning of left-to-right word;
# - If a cell is placed in the top row or the neighbouring upward cell is shaded, and neighbour down cell is empty,    then this cell is the beginning of up-to-down word.
# All words have a length greater than or equal to 3 letters. All empty cells should filled in.
# 
# You are given a crossword as a sequence of strings, where "X" is a shaded cell and "." is an empty cell.    You are also given the predefined list of words in lowercase.    (You can find ithereor    in the default code).    This list is the same for all crosswords and contains about 1500 nouns. You should use only the given words.
# 
# You don't need to find all of the possible solutions. It will be enough to find any solution which fills the    crossword puzzle and contains the correct words.
# 
# 
# 
# Input:Two arguments. A crossword as a tuple of strings and the words as a tuple of strings.
# 
# Output:Any solved variant of the crossword as a tuple/list of strings.
# 
# Precondition:
# 3 < len(crossword) ≤ 10
# all(3 < len(row) ≤ 10 and len(row) == len(crossword[0]) for row in crossword)
# 
# 
# END_DESC

def solver(crossword, words):
    return crossword


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    import string

    ERROR_TYPE = (False, "The result must be a list/tuple of strings")
    ERROR_SIZE = (False, "The result must have the same size as input data")
    ERROR_TEMPLATE = (False, "Your result is not look like the original crossword")
    ERROR_UNFILLED = (False, "I see the empty cell in your result")
    ERROR_TYPE_CELL = (False, "Cells should contains lowercase ascii letters or 'X'")
    F_ERROR_REPEATED = lambda w: (False, "Found repeated words '{}'".format(w))
    F_ERROR_UNKNOWN = lambda w: (False, "The word '{}' is not from the dictionary".format(w))
    WORDS = ['act', 'age', 'air', 'arm', 'art', 'ask', 'bad', 'bag', 'bar', 'bat', 'bed', 'bet', 'bid', 'big', 'bit', 'box', 'boy', 'bug', 'bus', 'buy', 'can', 'cap', 'car', 'cat', 'cow', 'cry', 'cup', 'cut', 'dad', 'day', 'dig', 'dog', 'dot', 'due', 'ear', 'eat', 'egg', 'end', 'eye', 'fan', 'fat', 'fee', 'few', 'fix', 'fly', 'fun', 'gap', 'gas', 'god', 'guy', 'hat', 'hit', 'ice', 'job', 'key', 'kid', 'lab', 'law', 'lay', 'leg', 'let', 'lie', 'lip', 'log', 'low', 'man', 'map', 'mix', 'mom', 'mud', 'net', 'oil', 'one', 'pay', 'pen', 'pie', 'pin', 'pop', 'pot', 'put', 'raw', 'red', 'rip', 'row', 'rub', 'run', 'sad', 'sea', 'set', 'sex', 'she', 'sir', 'sky', 'son', 'sun', 'tap', 'tax', 'tea', 'tie', 'tip', 'toe', 'top', 'try', 'two', 'use', 'war', 'way', 'web', 'win', 'you', 'area', 'army', 'baby', 'back', 'bake', 'ball', 'band', 'bank', 'base', 'bath', 'bear', 'beat', 'beer', 'bell', 'belt', 'bend', 'bike', 'bill', 'bird', 'bite', 'blow', 'blue', 'boat', 'body', 'bone', 'book', 'boot', 'boss', 'bowl', 'burn', 'cake', 'call', 'calm', 'camp', 'card', 'care', 'case', 'cash', 'cell', 'chip', 'city', 'club', 'clue', 'coat', 'code', 'cold', 'cook', 'copy', 'cost', 'crew', 'dare', 'dark', 'data', 'date', 'dead', 'deal', 'dear', 'debt', 'deep', 'desk', 'diet', 'dirt', 'dish', 'disk', 'door', 'drag', 'draw', 'drop', 'dump', 'dust', 'duty', 'ease', 'east', 'edge', 'exam', 'exit', 'face', 'fact', 'fall', 'farm', 'fear', 'feed', 'feel', 'file', 'fill', 'film', 'fire', 'fish', 'flow', 'fold', 'food', 'foot', 'form', 'fuel', 'gain', 'game', 'gate', 'gear', 'gene', 'gift', 'girl', 'give', 'glad', 'goal', 'gold', 'golf', 'good', 'grab', 'hair', 'half', 'hall', 'hand', 'hang', 'harm', 'hate', 'head', 'heat', 'hell', 'help', 'hide', 'high', 'hire', 'hold', 'hole', 'home', 'hook', 'hope', 'host', 'hour', 'hunt', 'hurt', 'idea', 'iron', 'item', 'join', 'joke', 'jump', 'jury', 'keep', 'kick', 'kill', 'kind', 'king', 'kiss', 'knee', 'lack', 'lady', 'lake', 'land', 'lead', 'life', 'lift', 'line', 'link', 'list', 'load', 'loan', 'lock', 'long', 'look', 'loss', 'love', 'luck', 'mail', 'main', 'make', 'male', 'mall', 'many', 'mark', 'mate', 'math', 'meal', 'meat', 'meet', 'menu', 'mess', 'milk', 'mind', 'mine', 'miss', 'mode', 'mood', 'most', 'move', 'nail', 'name', 'neat', 'neck', 'news', 'nose', 'note', 'oven', 'pace', 'pack', 'page', 'pain', 'pair', 'park', 'part', 'pass', 'past', 'path', 'peak', 'pick', 'pipe', 'plan', 'play', 'poem', 'poet', 'pool', 'post', 'pull', 'push', 'quit', 'race', 'rain', 'rate', 'read', 'rent', 'rest', 'rice', 'rich', 'ride', 'ring', 'rise', 'risk', 'road', 'rock', 'role', 'roll', 'roof', 'room', 'rope', 'ruin', 'rule', 'rush', 'safe', 'sail', 'sale', 'salt', 'sand', 'save', 'seat', 'self', 'sell', 'ship', 'shoe', 'shop', 'shot', 'show', 'sick', 'side', 'sign', 'sing', 'sink', 'site', 'size', 'skin', 'slip', 'snow', 'sock', 'soft', 'soil', 'song', 'sort', 'soup', 'spot', 'star', 'stay', 'step', 'stop', 'suck', 'suit', 'swim', 'tale', 'talk', 'tank', 'task', 'team', 'tear', 'tell', 'term', 'test', 'text', 'till', 'time', 'tone', 'tool', 'tour', 'town', 'tree', 'trip', 'tune', 'turn', 'type', 'unit', 'user', 'vast', 'verb', 'verb', 'verb', 'view', 'wait', 'wake', 'walk', 'wall', 'wash', 'wave', 'wear', 'week', 'west', 'wife', 'will', 'wind', 'wine', 'wing', 'wish', 'wood', 'word', 'work', 'wrap', 'yard', 'year', 'zone', 'abuse', 'actor', 'adult', 'agent', 'alarm', 'anger', 'angle', 'apple', 'aside', 'award', 'basis', 'beach', 'being', 'bench', 'birth', 'black', 'blame', 'blank', 'blind', 'block', 'blood', 'board', 'bonus', 'brain', 'brave', 'bread', 'break', 'brick', 'brief', 'broad', 'brown', 'brush', 'buddy', 'bunch', 'buyer', 'cable', 'candy', 'carry', 'catch', 'cause', 'chain', 'chair', 'chart', 'check', 'cheek', 'chest', 'child', 'claim', 'class', 'clerk', 'click', 'clock', 'cloud', 'coach', 'coast', 'count', 'court', 'cover', 'crack', 'craft', 'crash', 'crazy', 'cream', 'cross', 'curve', 'cycle', 'dance', 'death', 'delay', 'depth', 'devil', 'doubt', 'draft', 'drama', 'dream', 'dress', 'drink', 'drive', 'drunk', 'earth', 'entry', 'equal', 'error', 'essay', 'event', 'fault', 'field', 'fight', 'final', 'floor', 'focus', 'force', 'frame', 'front', 'fruit', 'funny', 'glass', 'glove', 'grade', 'grand', 'grass', 'great', 'green', 'group', 'guard', 'guess', 'guest', 'guide', 'habit', 'heart', 'heavy', 'hello', 'honey', 'horse', 'hotel', 'house', 'human', 'hurry', 'ideal', 'image', 'issue', 'joint', 'judge', 'juice', 'knife', 'laugh', 'layer', 'leave', 'level', 'light', 'limit', 'local', 'lunch', 'major', 'march', 'match', 'maybe', 'media', 'metal', 'might', 'minor', 'model', 'money', 'month', 'motor', 'mouse', 'mouth', 'movie', 'music', 'nasty', 'nerve', 'night', 'noise', 'north', 'novel', 'nurse', 'offer', 'order', 'other', 'owner', 'paint', 'panic', 'paper', 'party', 'pause', 'peace', 'phase', 'phone', 'photo', 'piano', 'piece', 'pitch', 'pizza', 'place', 'plane', 'plant', 'plate', 'point', 'pound', 'power', 'press', 'price', 'pride', 'print', 'prior', 'prize', 'proof', 'punch', 'queen', 'quiet', 'quote', 'radio', 'raise', 'range', 'ratio', 'reach', 'reply', 'river', 'rough', 'round', 'royal', 'salad', 'scale', 'scene', 'score', 'screw', 'sense', 'serve', 'shake', 'shame', 'shape', 'share', 'shift', 'shine', 'shirt', 'shock', 'shoot', 'silly', 'skill', 'skirt', 'sleep', 'slice', 'slide', 'smile', 'smoke', 'solid', 'sound', 'south', 'space', 'spare', 'speed', 'spell', 'spend', 'spite', 'split', 'sport', 'spray', 'staff', 'stage', 'stand', 'start', 'state', 'steak', 'steal', 'stick', 'still', 'stock', 'store', 'storm', 'story', 'strip', 'study', 'stuff', 'style', 'sugar', 'sweet', 'swing', 'table', 'taste', 'teach', 'theme', 'thing', 'title', 'today', 'tooth', 'topic', 'total', 'touch', 'tough', 'towel', 'tower', 'track', 'trade', 'train', 'trash', 'treat', 'trick', 'truck', 'trust', 'truth', 'twist', 'uncle', 'union', 'upper', 'usual', 'value', 'video', 'virus', 'visit', 'voice', 'watch', 'water', 'weird', 'wheel', 'while', 'white', 'whole', 'woman', 'world', 'worry', 'worth', 'young', 'youth', 'abroad', 'access', 'action', 'active', 'advice', 'affair', 'affect', 'agency', 'amount', 'animal', 'annual', 'answer', 'appeal', 'aspect', 'assist', 'attack', 'author', 'basket', 'battle', 'beyond', 'bitter', 'border', 'boring', 'bother', 'bottle', 'bottom', 'branch', 'breast', 'breath', 'bridge', 'budget', 'button', 'camera', 'cancel', 'cancer', 'candle', 'career', 'carpet', 'chance', 'change', 'charge', 'choice', 'church', 'client', 'closet', 'coffee', 'collar', 'common', 'cookie', 'corner', 'county', 'couple', 'course', 'cousin', 'credit', 'damage', 'dealer', 'debate', 'degree', 'demand', 'design', 'desire', 'detail', 'device', 'dinner', 'divide', 'doctor', 'double', 'drawer', 'driver', 'editor', 'effect', 'effort', 'employ', 'energy', 'engine', 'escape', 'estate', 'excuse', 'expert', 'extent', 'factor', 'family', 'farmer', 'father', 'female', 'figure', 'finger', 'finish', 'flight', 'flower', 'formal', 'friend', 'future', 'garage', 'garden', 'gather', 'ground', 'growth', 'guitar', 'handle', 'health', 'height', 'horror', 'impact', 'income', 'injury', 'insect', 'inside', 'invite', 'island', 'jacket', 'junior', 'ladder', 'lawyer', 'leader', 'league', 'length', 'lesson', 'letter', 'listen', 'living', 'manner', 'market', 'master', 'matter', 'medium', 'member', 'memory', 'method', 'middle', 'minute', 'mirror', 'mobile', 'moment', 'mother', 'muscle', 'nation', 'native', 'nature', 'nobody', 'normal', 'notice', 'number', 'object', 'office', 'option', 'orange', 'parent', 'people', 'period', 'permit', 'person', 'phrase', 'player', 'plenty', 'poetry', 'police', 'policy', 'potato', 'priest', 'profit', 'prompt', 'public', 'purple', 'reason', 'recipe', 'record', 'refuse', 'region', 'regret', 'relief', 'remote', 'remove', 'repair', 'repeat', 'report', 'resist', 'resort', 'result', 'return', 'reveal', 'review', 'reward', 'safety', 'salary', 'sample', 'scheme', 'school', 'screen', 'script', 'search', 'season', 'second', 'secret', 'sector', 'senior', 'series', 'shower', 'signal', 'silver', 'simple', 'singer', 'single', 'sister', 'source', 'speech', 'spirit', 'spread', 'spring', 'square', 'stable', 'status', 'strain', 'street', 'stress', 'strike', 'string', 'stroke', 'studio', 'stupid', 'summer', 'survey', 'switch', 'system', 'tackle', 'target', 'tennis', 'thanks', 'theory', 'throat', 'ticket', 'tongue', 'travel', 'unique', 'visual', 'volume', 'wealth', 'weight', 'window', 'winner', 'winter', 'wonder', 'worker', 'writer', 'yellow', 'ability', 'account', 'address', 'advance', 'airline', 'airport', 'alcohol', 'analyst', 'anxiety', 'anybody', 'arrival', 'article', 'article', 'attempt', 'average', 'balance', 'bedroom', 'benefit', 'bicycle', 'brother', 'cabinet', 'capital', 'channel', 'chapter', 'charity', 'chicken', 'classic', 'climate', 'clothes', 'college', 'combine', 'comfort', 'command', 'comment', 'company', 'complex', 'concept', 'concern', 'concert', 'consist', 'contact', 'contest', 'context', 'control', 'convert', 'counter', 'country', 'courage', 'culture', 'current', 'deposit', 'diamond', 'disease', 'display', 'drawing', 'economy', 'emotion', 'evening', 'example', 'extreme', 'failure', 'feature', 'feeling', 'finance', 'finding', 'fishing', 'forever', 'fortune', 'freedom', 'funeral', 'garbage', 'general', 'grocery', 'hearing', 'highway', 'history', 'holiday', 'housing', 'husband', 'illegal', 'impress', 'initial', 'kitchen', 'leading', 'leather', 'lecture', 'library', 'machine', 'manager', 'maximum', 'meaning', 'meeting', 'mention', 'message', 'minimum', 'mission', 'mistake', 'mixture', 'monitor', 'morning', 'natural', 'network', 'nothing', 'officer', 'opening', 'opinion', 'outcome', 'outside', 'package', 'parking', 'partner', 'passage', 'passion', 'patient', 'pattern', 'payment', 'penalty', 'pension', 'physics', 'picture', 'plastic', 'present', 'primary', 'private', 'problem', 'process', 'produce', 'product', 'profile', 'program', 'project', 'promise', 'purpose', 'quality', 'quarter', 'reading', 'reality', 'recover', 'regular', 'release', 'request', 'reserve', 'resolve', 'respect', 'respond', 'revenue', 'routine', 'savings', 'science', 'scratch', 'section', 'service', 'session', 'setting', 'shelter', 'society', 'speaker', 'special', 'station', 'stomach', 'storage', 'stretch', 'student', 'subject', 'success', 'support', 'surgery', 'suspect', 'teacher', 'tension', 'thought', 'tonight', 'tourist', 'traffic', 'trainer', 'trouble', 'variety', 'vehicle', 'version', 'village', 'warning', 'weather', 'wedding', 'weekend', 'welcome', 'western', 'whereas', 'witness', 'working', 'writing', 'accident', 'activity', 'addition', 'ambition', 'analysis', 'anything', 'anywhere', 'argument', 'attitude', 'audience', 'baseball', 'bathroom', 'birthday', 'building', 'business', 'calendar', 'campaign', 'category', 'champion', 'chemical', 'computer', 'conflict', 'constant', 'contract', 'creative', 'currency', 'customer', 'database', 'daughter', 'decision', 'delivery', 'designer', 'director', 'disaster', 'discount', 'distance', 'district', 'document', 'election', 'elevator', 'emphasis', 'employee', 'employer', 'engineer', 'entrance', 'estimate', 'evidence', 'exchange', 'exercise', 'external', 'familiar', 'feedback', 'football', 'function', 'guidance', 'homework', 'hospital', 'incident', 'increase', 'industry', 'instance', 'interest', 'internal', 'internet', 'judgment', 'language', 'location', 'magazine', 'marriage', 'material', 'medicine', 'midnight', 'mortgage', 'mountain', 'national', 'negative', 'occasion', 'official', 'opposite', 'ordinary', 'original', 'painting', 'patience', 'personal', 'physical', 'platform', 'pleasure', 'politics', 'position', 'positive', 'possible', 'practice', 'presence', 'pressure', 'priority', 'progress', 'property', 'proposal', 'purchase', 'quantity', 'question', 'reaction', 'register', 'relation', 'relative', 'republic', 'research', 'resident', 'resource', 'response', 'sandwich', 'schedule', 'security', 'sentence', 'shopping', 'shoulder', 'software', 'solution', 'specific', 'standard', 'stranger', 'strategy', 'strength', 'struggle', 'surprise', 'surround', 'swimming', 'sympathy', 'teaching', 'tomorrow', 'training', 'upstairs', 'vacation', 'valuable', 'weakness', 'advantage', 'afternoon', 'agreement', 'apartment', 'assistant', 'associate', 'attention', 'awareness', 'beautiful', 'beginning', 'boyfriend', 'breakfast', 'brilliant', 'candidate', 'challenge', 'character', 'chemistry', 'childhood', 'chocolate', 'cigarette', 'classroom', 'committee', 'community', 'complaint', 'condition', 'confusion', 'criticism', 'departure', 'dependent', 'dimension', 'direction', 'economics', 'education', 'effective', 'emergency', 'equipment', 'extension', 'following', 'guarantee', 'highlight', 'historian', 'implement', 'inflation', 'influence', 'inspector', 'insurance', 'intention', 'interview', 'knowledge', 'landscape', 'marketing', 'necessary', 'newspaper', 'objective', 'operation', 'passenger', 'pollution', 'potential', 'president', 'principle', 'procedure', 'professor', 'promotion', 'reception', 'recording', 'reference', 'secretary', 'selection', 'sensitive', 'signature', 'situation', 'somewhere', 'spiritual', 'statement', 'structure', 'substance', 'telephone', 'temporary', 'tradition', 'variation', 'vegetable', 'yesterday', 'appearance', 'assignment', 'assistance', 'assumption', 'atmosphere', 'background', 'collection', 'commercial', 'commission', 'comparison', 'conclusion', 'conference', 'confidence', 'connection', 'definition', 'department', 'depression', 'difference', 'difficulty', 'discipline', 'discussion', 'efficiency', 'employment', 'enthusiasm', 'equivalent', 'excitement', 'experience', 'expression', 'foundation', 'friendship', 'girlfriend', 'government', 'importance', 'impression', 'indication', 'individual', 'inevitable', 'initiative', 'inspection', 'investment', 'leadership', 'literature', 'management', 'membership', 'obligation', 'particular', 'percentage', 'perception', 'permission', 'philosophy', 'population', 'possession', 'preference', 'profession', 'protection', 'psychology', 'reflection', 'reputation', 'resolution', 'restaurant', 'revolution', 'specialist', 'suggestion', 'technology', 'television', 'transition', 'university', 'advertising', 'alternative', 'application', 'appointment', 'association', 'celebration', 'combination', 'comfortable', 'competition', 'concentrate', 'consequence', 'description', 'development', 'engineering', 'environment', 'examination', 'explanation', 'grandfather', 'grandmother', 'imagination', 'improvement', 'independent', 'information', 'instruction', 'interaction', 'maintenance', 'measurement', 'negotiation', 'opportunity', 'performance', 'personality', 'perspective', 'possibility', 'preparation', 'recognition', 'replacement', 'requirement', 'supermarket', 'temperature', 'championship', 'construction', 'contribution', 'conversation', 'distribution', 'independence', 'introduction', 'manufacturer', 'organization', 'presentation', 'professional', 'refrigerator', 'relationship', 'satisfaction', 'significance', 'communication', 'consideration', 'entertainment', 'establishment', 'international', 'understanding', 'administration', 'recommendation', 'representative', 'responsibility', 'transportation']

    def find_word(grid, row, col):
        word = ""
        while col < len(grid[row]) and grid[row][col] != "X":
            word += grid[row][col]
            col += 1
        return word

    def checker(func, template):
        result = func(template, WORDS)
        # types check
        if not isinstance(result, (tuple, list)):
            return ERROR_TYPE
        if not all(isinstance(row, str) for row in result):
            return ERROR_TYPE

        # size check
        if (len(result) != len(template) or
                any(len(result[i]) != len(template[i]) for i in range(len(template)))):
            return ERROR_SIZE

        # template, letters and filled check
        for i, row in enumerate(result):
            for j, ch in enumerate(row):
                if ch == "X":
                    if template[i][j] != "X":
                        return ERROR_TEMPLATE
                elif ch == ".":
                    return ERROR_UNFILLED
                elif ch in string.ascii_lowercase:
                    if template[i][j] != ".":
                        return ERROR_TEMPLATE
                else:
                    return ERROR_TYPE_CELL

        # words checking
        used_words = set()
        rotated_result = ["".join(row) for row in zip(*result)]

        words = []
        for k, row in enumerate(template):
            for m, symb in enumerate(row):
                if symb == "X":
                    continue
                if (k == 0 or template[k - 1][m] == "X") and (k < len(template) - 1 and template[k + 1][m] == "."):
                    words.append(find_word(rotated_result, m, k))
                if (m == 0 or template[k][m - 1] == "X") and (m < len(template[k]) - 1 and template[k][m + 1] == "."):
                    words.append(find_word(result, k, m))
        for w in words:
            if w in used_words:
                return F_ERROR_REPEATED(w)
            used_words.add(w)
            if w not in WORDS:
                return F_ERROR_UNKNOWN(w)
        return True, "Great!"

    result, message = checker(solver, ['.XXX.', '...X.', '.X.X.', '.....'])
    assert result, "1st example. " + message

    result, message = checker(solver, ['X.XX', '....', 'X.XX', 'X...', 'XXX.', '....', 'XXX.'],)
    assert result, "2nd example. " + message

    result, message = checker(solver, ['...XXXXXX', '.XXX.X...', '.....X.XX', 'XXXX.X...',
                                       'XX...X.XX', 'XX.XXX.X.', 'X......X.', 'XX.X.XXX.', 'XXXX.....'],)
    assert result, "3rd example. " + message