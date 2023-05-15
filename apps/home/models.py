# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Cliente(models.Model):
    cpf = models.CharField(max_length=14)
    nome = models.CharField(max_length=50)
    logradouro = models.CharField(max_length=50, blank=True, null=True)
    numero = models.CharField(max_length=14, blank=True, null=True)
    cep = models.CharField(max_length=8, blank=True, null=True)
    bairro = models.CharField(max_length=30, blank=True, null=True)
    cidade = models.CharField(max_length=30, blank=True, null=True)
    estado = models.CharField(max_length=2, blank=True, null=True)
    complemento = models.CharField(max_length=30, blank=True, null=True)
    pais = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=30, blank=True, null=True)
    telefone = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'cliente'


class Estabelecimento(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    cnpj = models.CharField(db_column='CNPJ', max_length=50)  # Field name made lowercase.
    nomefantasia = models.CharField(db_column='NomeFantasia', max_length=50, blank=True, null=True)  # Field name made lowercase.
    logradouro = models.CharField(db_column='Logradouro', max_length=50, blank=True, null=True)  # Field name made lowercase.
    numero = models.CharField(db_column='Numero', max_length=50, blank=True, null=True)  # Field name made lowercase.
    complemento = models.CharField(db_column='Complemento', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bairro = models.CharField(db_column='Bairro', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cidade = models.CharField(db_column='Cidade', max_length=50, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=2, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    telefone = models.CharField(db_column='Telefone', max_length=30, blank=True, null=True)  # Field name made lowercase.
    loja = models.IntegerField(db_column='Loja')  # Field name made lowercase.
    oficina = models.IntegerField(db_column='Oficina')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'estabelecimento'


class Estoque(models.Model):
    idproduto = models.ForeignKey('Produto', models.DO_NOTHING, db_column='idProduto')  # Field name made lowercase.
    idestabelecimento = models.ForeignKey(Estabelecimento, models.DO_NOTHING, db_column='idEstabelecimento')  # Field name made lowercase.
    quantidade = models.PositiveIntegerField()
    localizacao = models.CharField(max_length=50, blank=True, null=True)
    qtd_minima = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'estoque'


class Fornecedor(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    cnpj = models.CharField(db_column='CNPJ', max_length=50)  # Field name made lowercase.
    nomefantasia = models.CharField(db_column='NomeFantasia', max_length=50, blank=True, null=True)  # Field name made lowercase.
    logradouro = models.CharField(db_column='Logradouro', max_length=50, blank=True, null=True)  # Field name made lowercase.
    numero = models.CharField(db_column='Numero', max_length=50, blank=True, null=True)  # Field name made lowercase.
    complemento = models.CharField(db_column='Complemento', max_length=50, blank=True, null=True)  # Field name made lowercase.
    bairro = models.CharField(db_column='Bairro', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cep = models.CharField(db_column='CEP', max_length=50, blank=True, null=True)  # Field name made lowercase.
    cidade = models.CharField(db_column='Cidade', max_length=50, blank=True, null=True)  # Field name made lowercase.
    estado = models.CharField(db_column='Estado', max_length=2, blank=True, null=True)  # Field name made lowercase.
    email = models.CharField(db_column='Email', max_length=50, blank=True, null=True)  # Field name made lowercase.
    telefone = models.CharField(db_column='Telefone', max_length=30, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'fornecedor'


class Moto(models.Model):
    placa = models.CharField(max_length=50)
    ano = models.CharField(max_length=50, blank=True, null=True)
    modeloid = models.ForeignKey('Motomodelo', models.DO_NOTHING, db_column='modeloId')  # Field name made lowercase.
    km = models.CharField(max_length=50, blank=True, null=True)
    cor = models.CharField(max_length=50, blank=True, null=True)
    chassi = models.CharField(max_length=50, blank=True, null=True)
    renavam = models.CharField(max_length=50, blank=True, null=True)
    clienteid = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='clienteId')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'moto'


class Motomarca(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'motomarca'


class Motomodelo(models.Model):
    nome = models.CharField(max_length=50)
    marcaid = models.ForeignKey(Motomarca, models.DO_NOTHING, db_column='marcaId')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'motomodelo'


class Produto(models.Model):
    item = models.CharField(max_length=50)
    marca = models.CharField(max_length=50)
    fabricante = models.CharField(max_length=50)
    codigo = models.CharField(max_length=50)
    custo = models.DecimalField(max_digits=16, decimal_places=2)
    valor = models.DecimalField(max_digits=16, decimal_places=2)
    ano = models.CharField(max_length=50, blank=True, null=True)
    idcategoria = models.ForeignKey('Produtocategoria', models.DO_NOTHING, db_column='idCategoria')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'produto'


class ProdutoMotomodelo(models.Model):
    idproduto = models.ForeignKey(Produto, models.DO_NOTHING, db_column='idProduto')  # Field name made lowercase.
    idmotomodelo = models.ForeignKey(Motomodelo, models.DO_NOTHING, db_column='idMotoModelo')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'produto_motomodelo'


class Produtocategoria(models.Model):
    nome = models.CharField(max_length=50)

    class Meta:
        managed = True
        db_table = 'produtocategoria'


class Servico(models.Model):
    descriminacao = models.CharField(max_length=50, blank=True, null=True)
    codigo = models.CharField(max_length=50, blank=True, null=True)
    valor = models.DecimalField(max_digits=19, decimal_places=2, blank=True, null=True)
    comissao = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'servico'


class Usuario(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nome = models.CharField(db_column='Nome', max_length=50)  # Field name made lowercase.
    email = models.CharField(db_column='Email', unique=True, max_length=50)  # Field name made lowercase.
    salt = models.CharField(db_column='Salt', max_length=100)  # Field name made lowercase.
    hash = models.CharField(db_column='Hash', max_length=100)  # Field name made lowercase.
    idestabelecimento = models.ForeignKey(Estabelecimento, models.DO_NOTHING, db_column='IdEstabelecimento', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'usuario'


class Venda(models.Model):
    datacriacao = models.DateTimeField(db_column='dataCriacao')  # Field name made lowercase.
    motoid = models.ForeignKey(Moto, models.DO_NOTHING, db_column='motoId', blank=True, null=True)  # Field name made lowercase.
    clienteid = models.ForeignKey(Cliente, models.DO_NOTHING, db_column='clienteId', blank=True, null=True)  # Field name made lowercase.
    valor = models.DecimalField(max_digits=19, decimal_places=2)
    status = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'venda'


class Vendaproduto(models.Model):
    vendaid = models.ForeignKey(Venda, models.DO_NOTHING, db_column='vendaId')  # Field name made lowercase.
    produtoid = models.ForeignKey(Produto, models.DO_NOTHING, db_column='produtoId')  # Field name made lowercase.
    quantidade = models.IntegerField()

    class Meta:
        managed = True
        db_table = 'vendaproduto'


class Vendaservico(models.Model):
    vendaid = models.ForeignKey(Venda, models.DO_NOTHING, db_column='vendaId')  # Field name made lowercase.
    servicoid = models.ForeignKey(Servico, models.DO_NOTHING, db_column='servicoId')  # Field name made lowercase.
    quantidade = models.IntegerField()
    valor = models.DecimalField(max_digits=19, decimal_places=2)

    class Meta:
        managed = True
        db_table = 'vendaservico'
