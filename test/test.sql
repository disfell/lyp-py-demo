REPLACE INTO gfuser.gfservice (service_id, service_name, password_type, access_level, serv_busi_type, serv_busi_prop, serv_flag_str, reststart_time, restend_time, en_sys_status, scan_task_type, busin_type) VALUES
(1000467, '二级后台费用按模板查询', '0', '1', '0', '0', '0100', 0, 0, '12', '', ''),
(1000468, '二级债券费用按模板查询', '0', '1', '0', '0', '0100', 0, 0, '12', '', ''),
(1000469, '港股费用按模板查询', '0', '1', '0', '0', '0100', 0, 0, '12', '', ''),
(1000470, '二级回购费用按模板查询', '0', '1', '0', '0', '0100', 0, 0, '12', '', ''),
(1000471, '二级基金费用按模板查询', '0', '1', '0', '0', '0100', 0, 0, '12', '', ''),
(1000472, '大宗交易费用按模板查询', '0', '1', '0', '0', '0100', 0, 0, '12', '', ''),
(1000473, '北证股转交易费用按模板查询', '0', '1', '0', '0', '0100', 0, 0, '12', '', ''),
(1000474, '融资融券后台费用按模板查询', '0', '1', '0', '0', '0100', 0, 0, '12', '', ''),
(1000475, '融资融券债券费用按模板查询', '0', '1', '0', '0', '0100', 0, 0, '12', '', ''),
(1000476, '融资融券基金费用按模板查询', '0', '1', '0', '0', '0100', 0, 0, '12', '', '');

REPLACE INTO gfsettle.queryconfig (uri, target, nec_params, service_id, qry_sql, update_time, remark) VALUES
('queryBfare2ByFareKind', '0', 'fare_kind', '1000467',
'SELECT * FROM HS_USER.BFARE2 b WHERE 1=1
	AND b.FARE_KIND = :fare_kind
	AND b.STOCK_TYPE IN (''0'',''6'',''c'',''d'',''e'',''g'',''h'',''3'',''p'',''q'')
	AND b.EXCHANGE_TYPE IN (''1'',''2'',''D'',''H'', ''R'')
ORDER by b.EXCHANGE_TYPE, b.STOCK_TYPE', DATE_FORMAT(NOW(), '%Y%m%d'), '(BOPS-34907)二级后台费用按模板查询'),
('queryZfare2ByFareKind', '0', 'fare_kind', '1000468',
'SELECT * FROM HS_USER.BFARE2 b WHERE 1=1
	AND b.FARE_KIND = :fare_kind
	AND b.STOCK_TYPE  IN (''9'',''X'',''U'',''Y'',''u'',''a'',''w'',''r'')
	AND b.EXCHANGE_TYPE IN (''1'',''2'')
ORDER by b.EXCHANGE_TYPE, b.STOCK_TYPE', DATE_FORMAT(NOW(), '%Y%m%d'), '(BOPS-34907)二级债券费用按模板查询'),
('querGGfare2ByFareKind', '0', 'fare_kind', '1000469',
'SELECT * FROM HS_USER.BFARE2 b WHERE 1=1
	AND b.FARE_KIND = :fare_kind
	AND b.STOCK_TYPE  IN (''0'', ''3'', ''T'')
	AND b.EXCHANGE_TYPE IN (''G'',''S'')
ORDER by b.EXCHANGE_TYPE, b.STOCK_TYPE', DATE_FORMAT(NOW(), '%Y%m%d'), '(BOPS-34907)港股费用按模板查询'),
('queryHfare2ByFareKind', '0', 'fare_kind', '1000470',
'SELECT * FROM HS_USER.HFARE2 h WHERE 1=1
	AND h.FARE_KIND = :fare_kind
ORDER by h.EXCHANGE_TYPE', DATE_FORMAT(NOW(), '%Y%m%d'), '(BOPS-34907)二级回购费用按模板查询'),
('queryOffare2ByFareKind', '0', 'fare_kind', '1000471',
'SELECT * FROM HS_USER.OFFARE2 o WHERE 1=1
	AND o.FARE_KIND = :fare_kind
	AND o.STOCK_TYPE IN (''A'',''J'',''K'',''L'',''M'',''N'',''T'',''i'',''j'',''k'',''l'',''m'',''r'')
	AND o.EXCHANGE_TYPE IN (''1'',''2'')
ORDER by o.EXCHANGE_TYPE, o.STOCK_TYPE', DATE_FORMAT(NOW(), '%Y%m%d'), '(BOPS-34907)二级基金费用按模板查询'),
('queryDfare2ByFareKind', '0', 'fare_kind', '1000472',
'SELECT * FROM HS_USER.DFARE2 d WHERE 1=1
	AND d.FARE_KIND = :fare_kind
	AND d.STOCK_TYPE IN (''0'',''c'',''z'',''6'',''9'',''Q'',''U'',''X'',''Y'',''Z'',''u'',''T'',''L'',''D'',''a'',''j'',''l'',''d'',''e'',''g'',''h'',''3'',''p'',''q'',''r'')
	AND d.EXCHANGE_TYPE IN (''1'',''2'',''D'',''H'', ''R'')
ORDER by d.EXCHANGE_TYPE, d.STOCK_TYPE', DATE_FORMAT(NOW(), '%Y%m%d'), '(BOPS-34907)大宗交易费用按模板查询'),
('queryStbfare2ByFareKind', '0', 'fare_kind', '1000473',
'SELECT * FROM HS_USER.STBFARE2 stb WHERE 1=1
	AND stb.FARE_KIND = :fare_kind
	AND stb.EXCHANGE_TYPE IN (''9'',''A'')
ORDER by stb.EXCHANGE_TYPE, stb.STOCK_TYPE', DATE_FORMAT(NOW(), '%Y%m%d'), '(BOPS-34907)北证股转交易费用按模板查询'),
('queryCfare2ByFareKind', '0', 'fare_kind', '1000474',
'SELECT * FROM HS_USER.CFARE2 c WHERE 1=1
	AND c.FARE_KIND = :fare_kind
	AND c.STOCK_TYPE IN (''0'',''6'',''c'',''z'',''d'',''e'',''g'',''p'',''q'')
	AND c.EXCHANGE_TYPE IN (''1'',''2'',''9'')
ORDER by c.EXCHANGE_TYPE, c.STOCK_TYPE', DATE_FORMAT(NOW(), '%Y%m%d'), '(BOPS-34907)融资融券后台费用按模板查询'),
('queryCzfare2ByFareKind', '0', 'fare_kind', '1000475',
'SELECT * FROM HS_USER.CFARE2 c WHERE 1=1
	AND c.FARE_KIND = :fare_kind
	AND c.STOCK_TYPE IN (''9'',''Y'',''U'',''u'',''a'',''X'')
	AND c.EXCHANGE_TYPE IN (''1'',''2'')
ORDER by c.EXCHANGE_TYPE, c.STOCK_TYPE', DATE_FORMAT(NOW(), '%Y%m%d'), '(BOPS-34907)融资融券债券费用按模板查询'),
('queryCoffare2ByFareKind', '0', 'fare_kind', '1000476',
'SELECT * FROM HS_USER.COFFARE2 c WHERE 1=1
	AND c.FARE_KIND = :fare_kind
	AND c.STOCK_TYPE IN (''K'',''L'',''M'',''N'',''T'',''i'',''j'',''k'',''l'',''r'')
	AND c.EXCHANGE_TYPE IN (''1'',''2'')
ORDER by c.EXCHANGE_TYPE, c.STOCK_TYPE', DATE_FORMAT(NOW(), '%Y%m%d'), '(BOPS-34907)融资融券基金费用按模板查询');