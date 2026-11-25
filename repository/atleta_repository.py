# SQL puro do CRUD de Atlestas

from database.conexao import conectar

def inserir_atleta(nome, idade, modalidade):
    """Cadastra um atleta."""
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        sql = """
            INSERT INTO atleta (nome, idade, modalidade)
            VALUES (%s, %s, %s)
        """
        cursor.execute(sql, (nome, idade, modalidade))
        conexao.commit()
        return cursor.lastrowid
    except Exception:
        conexao.rollback()
        raise
    finally:
        cursor.close()
        conexao.close()


def listar_atletas():
    """Retorna todos os atletas como uma lista de dicionários."""
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    try:
        cursor.execute("SELECT * FROM atleta")
        return cursor.fetchall()
    finally:
        cursor.close()
        conexao.close()


def buscar_atleta(id_atleta):
    """Busca um atleta pelo ID."""
    conexao = conectar()
    cursor = conexao.cursor(dictionary=True)
    try:
        cursor.execute(
            "SELECT * FROM atleta WHERE id_atleta = %s",
            (id_atleta,)
        )
        return cursor.fetchone()
    finally:
        cursor.close()
        conexao.close()


def atualizar_atleta(id_atleta, nome, idade, modalidade):
    """Atualiza os dados de um atleta."""
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        sql = """
            UPDATE atleta
            SET nome = %s, idade = %s, modalidade = %s
            WHERE id_atleta = %s
        """
        cursor.execute(sql, (nome, idade, modalidade, id_atleta))
        conexao.commit()
        return cursor.rowcount
    except Exception:
        conexao.rollback()
        raise
    finally:
        cursor.close()
        conexao.close()


def excluir_atleta(id_atleta):
    """Exclui um atleta pelo ID."""
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute(
            "DELETE FROM atleta WHERE id_atleta = %s",
            (id_atleta,)
        )
        conexao.commit()
        return cursor.rowcount
    except Exception:
        conexao.rollback()
        raise
    finally:
        cursor.close()
        conexao.close()
