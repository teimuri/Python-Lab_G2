#! /bin/bash
conda remove --name <enname> --all
conda create --name <enname>
conda deactivate
conda activate <enname>
