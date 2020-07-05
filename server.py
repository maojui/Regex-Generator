import socketio
from aiohttp import web
import random
from src.parser import *
from src.genetic import genotype, crossover, mutation, nextGeneration

# creates a new Async Socket IO Server
sio = socketio.AsyncServer()
# Creates a new Aiohttp Web Application
app = web.Application()
# Binds our Socket.IO server to our Web App
sio.attach(app)

# we can define aiohttp endpoints just as we normally
# would with no change
async def index(request):
    with open('index.html') as f:
        return web.Response(text=f.read(), content_type='text/html')

def reject(message):
    res = {'ERROR' : message}
    return res

# If we wanted to create a new websocket endpoint,
# use this decorator, passing in the name of the
# event we wish to listen out for
@sio.on('start')
async def print_message(sid, message):
    print("Socket ID: " , sid)
    target = message['target'].split('\n')
    GENERATION = int(message['generation'])
    POPULATION = int(message['population'])
    match = int(message['match'])
    if not 30 >= GENERATION >= 1 : 
        await sio.emit('output', reject('Invalid generation.'))
        return
    if not 100 >= POPULATION >= 10 : 
        await sio.emit('output', reject('Invalid population size.'))
        return
    if match != None and not POPULATION >= match >= 0 : 
        await sio.emit('output', reject('match numbers must > 0 and smaller than populations'))
        return
    g = 1
    result = []
    MAX_FITNESS = -1e9
    BEST_GENE = None
    if match == None or match > len(target) :
        match = len(target)
    BEST_REGEX = ""
    gene_count = len(genotype)
    pop = [random.sample(range(0,gene_count), gene_count) for _ in range(POPULATION)] 
    for i in range(1,GENERATION+1) :
        
        arr, filtered_set = preprocessor(random.sample(target,match))
        # Get result
        current_generation = []
        for idx, gene in enumerate(pop):
            g_res, fitness = parser(arr, filtered_set, gene)
            result.append((fitness, ''.join(g_res)))
            current_generation.append((fitness, ''.join(g_res)))
            if fitness > MAX_FITNESS:
                MAX_FITNESS = fitness
                BEST_GENE = gene
                BEST_REGEX = ''.join(g_res)

        await sio.emit('output',sorted( set(result),key=lambda x : -x[0] ))

        # Next generation
        fitness = [g[0] for g in current_generation]
        pop = nextGeneration(pop, fitness)

# We bind our aiohttp endpoint to our app router
app.router.add_get('/', index)

# We kick off our server
if __name__ == '__main__':
    web.run_app(app, host="0.0.0.0", port=8080)