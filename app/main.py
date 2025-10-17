import tabula
import pandas as pd

pdf_path = "contas_agua_2025.pdf"

tabelas = tabula.read_pdf(pdf_path, pages="all", multiple_tables=True)

df_final = pd.concat(tabelas, ignore_index=True)

df_final.to_excel("contas_agua_2025.xlsx", index=False)

print("✅ Conversão concluída! Arquivo salvo como 'contas_agua_2025.xlsx'")