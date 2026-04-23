# -*- coding: utf-8 -*-
"""
Created on Thu Apr 23 15:44:59 2026

@author: jpfab
"""

import numpy as np


def CondSis(C, r = 0): # Condição do Sistema
  """
  Essa função analisa a condição da concentração de reagente no sistema, 
  considerando valores entre 0 e 10 mol/L.

  C: concentração do reagente em mol/L.
  r: número da leitura.
  cond: condição do sistema.
  """

  if C > 10 or C < 0:
    # Leitura inválida
    raise ValueError("A concentração deve ser entre 0 e 10 mol/L")
  
  elif C > 7:
    cond = "Alta"

  elif C >= 3:
    cond = "Adequada"

  else:
    cond = "Baixa"

  print(f"Leitura {r}:")
  print(f"  Concentração de reagente = {C:.4f} mol/L") # 0.0000
  print(f"  Condição do sistema: {cond}\n") # Alta, Adequada ou Baixa

  return cond
  

def Sim(n): # Simulação
  """
  Essa função simula leituras de concentração de reagente no sistema, 
  considerando valores entre 0 e 10 mol/L.

  n: número de simulações desejadas.
  C: concentração do reagente em mol/L.
  r: número da leitura.
  cond: condição do sistema.
  cont: dicionário com as ocorrências de cada condição de concentração.
  """

  cont = {'Alta': 0, 'Adequada': 0, 'Baixa': 0} # Dicionário de contadores

  print("="*60)
  print(f"Simulação de {n} entradas")
  print("="*60 + "\n")

  for i in range(n):
    C = np.random.uniform(0, 10) # Número aleatório contínuo entre 0 e 10
    r = i + 1 # i = 0 -> primeira leitura

    cond = CondSis(C, r) # Alta, Adequada ou Baixa
    cont[cond] += 1 # Adiciona 1 ao contador correspondente a condição

  return cont


def Res(cont): # Resumo
  """
  Essa função exibe um resumo das ocorrências de cada condição de 
  concentração, indicando a frequência de cada e a condição predominante.

  cont: dicionário com as ocorrências de cada condição de concentração.
  """

  print("="*60)
  print("Resumo")
  print("="*60 + "\n")

  print(f"  Concentração Alta: {cont['Alta']} ocorrências")
  print(f"  Concentração Adequada: {cont['Adequada']} ocorrências")  
  print(f"  Concentração Baixa: {cont['Baixa']} ocorrências")
  print(f"\n  Concentração Predominante: {max(cont, key=cont.get)}")
  # Nota ética: tive que pesquisar como utilizar a função max em um dicinário
  # max(dicionário, key=dicionário.get) -> pega a chave do maior valor


Res(Sim(10))
