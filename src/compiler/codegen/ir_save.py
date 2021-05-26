import sys
sys.path.append('src/compiler')

def ir_save(ir_str, name_file):
  path = f'result/{name_file}.ll'
  ir_result = open(path, 'w')

  ir_result.write(ir_str)