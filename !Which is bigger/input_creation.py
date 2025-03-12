import os
import shutil


heights = [0] + [0.529, -0.529] + [x for i in range(1, 10) for x in (i * 0.5, -i * 0.5)]
fchk_file = "benzene.fchk"

def format_name(value):
    return str(value).replace(".", "_")

def create_input_file(folder, x):
    filename = f"gdma_{folder}.input"
    content = f"""
File {fchk_file} Density MP2
Angstrom
Multipoles
  Limit 2
  Switch 4.0
  Radius H 0.35
  Punch file.punch
  Add TOP{x} 0.0 0.0  {x:.3f}
  ADD TOP{x} 0.0 0.0  {-x:.3f}
Start
Finish
""".strip()
    with open(os.path.join(folder, filename), "w", newline='\n') as f:
        f.write(content)

def create_sub_file(folder, x):
    filename = f"gdma_{folder}.sub"
    content = f"""
#!/bin/bash
#SBATCH --job-name=gdma_{folder}
#SBATCH --partition=normal
#SBATCH --nodes=1
#SBATCH --ntasks-per-node=2
#SBATCH --time=720:00:00

module load gdma/2.3.3

export SLURM_SUBMIT_DIR=$SLURM_SUBMIT_DIR
cd $SLURM_SUBMIT_DIR
gdma < gdma_{folder}.input > gdma_{folder}.output
""".strip()
    with open(os.path.join(folder, filename), "w", newline='\n') as f:
        f.write(content)


for i in range(len(heights)):
    if heights[i] == 0:
        folder = "0"
    else:
        x = heights[i]
        folder = f"{format_name(abs(x))}AND-{format_name(abs(x))}"
    
    os.makedirs(folder, exist_ok=True)
    create_input_file(folder, 0 if heights[i] == 0 else x)
    create_sub_file(folder, 0 if heights[i] == 0 else x)

    # Copia o arquivo fchk_file para dentro da pasta criada
    shutil.copy(fchk_file, os.path.join(folder, fchk_file))