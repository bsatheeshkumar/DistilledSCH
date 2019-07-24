import petl as etl
readFile = etl.fromtsv("donedeal_data_sample.tsv")
tmpTable = etl.addfield(readFile, 'InKms', lambda rec: rec['mileage'])
tmpTable2File = etl.convert(tmpTable, 'InKms', lambda v: int(float(v) * 1.6), where=lambda r: r.mileageType == 'miles')
etl.totsv(tmpTable2File, 'donedeal_inKms.tsv')