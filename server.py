import socketio
from aiohttp import web
import random
from parser import *
from genetic import genotype, crossover, mutation, nextGeneration

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

# If we wanted to create a new websocket endpoint,
# use this decorator, passing in the name of the
# event we wish to listen out for
@sio.on('start')
async def print_message(sid, message):
    print("Socket ID: " , sid)
    await sio.emit('output', message['target'][::-1])
    target = message['target'].split('\n')
    POPULATION = 100
    GENERATION = 10
    g = 1
    result = []
    MAX_FITNESS = -1e9
    BEST_GENE = None
    match = 1e9
    if match == None or match > len(target) :
        match = len(target)
    BEST_REGEX = ""
    gene_count = len(genotype)
    pop = [random.sample(range(0,gene_count), gene_count) for _ in range(POPULATION)] 
    for i in range(1,GENERATION+1) :
        
        # Get result
        current_generation = []
        for idx, gene in enumerate(pop):
            print(random.sample(target,k=match))
            g_res, fitness = parser(random.sample(target,match), gene)
            result.append((fitness, ''.join(g_res)))
            current_generation.append((fitness, ''.join(g_res)))
            if fitness > MAX_FITNESS:
                MAX_FITNESS = fitness
                BEST_GENE = gene
                BEST_REGEX = ''.join(g_res)

        await sio.emit('output',sorted( set(result),key=lambda x : -x[0] ))
        # for fit, regex in  sorted( set(result),key=lambda x : -x[0] )[:20]:
        #     print(f'{fit}\t\t{regex}')
        print(f'{i} Generation :')
        print(f'{MAX_FITNESS} {BEST_REGEX}')
        print(current_generation)
        # Next generation
        total = sum([g[0] for g in current_generation])
        prob = [g[0]/total for g in current_generation]
        pop = nextGeneration(pop, prob)

    return result
    
# We bind our aiohttp endpoint to our app router
app.router.add_get('/', index)

# We kick off our server
if __name__ == '__main__':
    web.run_app(app)