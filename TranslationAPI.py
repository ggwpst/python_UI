import subprocess


def anime2real(path, savePath = 'test.png'):
    subprocess.call(['python', f'translations/anime2real.py','--path',f'{path}','--savepath',f'{savePath}'])

def real2anime(path, savePath = 'test.png'):
    subprocess.call(['python', f'translations/real2anime.py','--path',f'{path}','--savepath',f'{savePath}'])

def real2jojo(path, savePath = 'test.png'):
    subprocess.call(['python', f'translations/real2jojo.py','--path',f'{path}','--savepath',f'{savePath}'])

def real2titan(path, savePath = 'test.png'):
    subprocess.call(['python', f'translations/real2titan.py','--path',f'{path}','--savepath',f'{savePath}'])
  
def real2gyate(path, savePath = 'test.png'):
    subprocess.call(['python', f'translations/real2gyate.py','--path',f'{path}','--savepath',f'{savePath}'])