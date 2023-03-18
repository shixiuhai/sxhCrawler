## 使用sql

```bash

(SELECT
	
  id,
	cate_name,
	cate_id ,
	count(cate_id)
FROM
	1688_kj_commodity_index 
WHERE
	cate_id NOT IN ( SELECT parent_id FROM 1688_kj_commodity_index )  GROUP BY id) 
	
	
	SELECT
	
  id,
	cate_name,
	cate_id ,
	count(cate_id)
FROM
	1688_kj_commodity_index 
WHERE
	cate_id NOT IN ( SELECT parent_id FROM 1688_kj_commodity_index )  GROUP BY id
	
	
	
-- 查询源表数据
SELECT
	id,
	cate_name,
	cate_id,
	cate_level,
	parent_id
FROM
	1688_kj_commodity_index 



-- 查询最后一级是二级的数据
SELECT
	id,
	cate_name,
	cate_id,
	cate_level,
	parent_id
FROM
	1688_kj_commodity_index 
WHERE
	cate_id NOT IN ( SELECT parent_id FROM 1688_kj_commodity_index ) 
	AND cate_level =2

	
-- 查询最后一级是三级的数据
SELECT
	id,
	cate_name,
	cate_id,
	cate_level,
	parent_id
FROM
	1688_kj_commodity_index 
WHERE
	cate_id NOT IN ( SELECT parent_id FROM 1688_kj_commodity_index ) 
	AND cate_level =1
	
	
-- 原表和 最后一级是三级的数据连表 查询出二级标题
SELECT
	table1.cate_name two_cate_name,
	table3.cate_name three_cate_name,
	table1.parent_id  two_parent_id,
-- 	这个cate_id 是最后一级的cate_id
	table3.cate_id
FROM
	( SELECT id, cate_name, cate_id, cate_level, parent_id FROM 1688_kj_commodity_index ) table1
	INNER JOIN ( SELECT id, cate_name, cate_id, cate_level, parent_id FROM 1688_kj_commodity_index WHERE cate_id NOT IN ( SELECT parent_id FROM 1688_kj_commodity_index ) AND cate_level =3 ) table3 ON table3.parent_id = table1.cate_id
	


-- 查询出最后一级是3级标题的所有内容
-- 原表和 （原表和最后一级是三级的数据连表） 进行一级标题查询
-- 查询出最后一级是3级标题的所有内容
-- 原表和 （原表和最后一级是三级的数据连表） 进行一级标题查询
SELECT
	-- 	针对cate_id去重不知道原因为什么
	 DISTINCT(b.cate_id),
	b.one_cate_name,
	b.two_cate_name,
	b.three_cate_name 
FROM
	(
	SELECT
		table1.cate_name one_cate_name,
		table1_3.two_cate_name,
		table1_3.three_cate_name,-- 最后一级的cate_id
		table1_3.cate_id 
	FROM
		( SELECT id, cate_name, cate_id, cate_level, parent_id FROM 1688_kj_commodity_index ) table1
		INNER JOIN (
		SELECT
			table1.cate_name two_cate_name,
			table3.cate_name three_cate_name,
			table1.parent_id two_parent_id,-- 	这个cate_id 是最后一级的cate_id
			table3.cate_id 
		FROM
			( SELECT id, cate_name, cate_id, cate_level, parent_id FROM 1688_kj_commodity_index ) table1
			INNER JOIN ( SELECT id, cate_name, cate_id, cate_level, parent_id FROM 1688_kj_commodity_index WHERE cate_id NOT IN ( SELECT parent_id FROM 1688_kj_commodity_index ) AND cate_level = 3 ) table3 ON table3.parent_id = table1.cate_id 
		) table1_3 ON table1_3.two_parent_id = table1.cate_id 
	) b 



-- 查询出最后一级id是二级的内容
SELECT
	table1.cate_name one_cate_name,
	table3.cate_name two_cate_name,
	'' three_cate_name,-- 	这个cate_id 是最后一级的cate_id
	table3.cate_id 
FROM
	( SELECT id, cate_name, cate_id, cate_level, parent_id FROM 1688_kj_commodity_index ) table1
	INNER JOIN ( SELECT id, cate_name, cate_id, cate_level, parent_id FROM 1688_kj_commodity_index WHERE cate_id NOT IN ( SELECT parent_id FROM 1688_kj_commodity_index ) AND cate_level = 2 ) table3 ON table3.parent_id = table1.cate_id
	
	
	
	
-- 基于最后一级是二级标题和最后一级是三级标题的所有数据合并
SELECT
	table1_2_3.* 
FROM
	(
		SELECT-- 	针对cate_id去重不知道原因为什么
		DISTINCT ( b.cate_id ),
		b.one_cate_name,
		b.two_cate_name,
		b.three_cate_name
		
	FROM
		(
		SELECT
			table1.cate_name one_cate_name,
			table1_3.two_cate_name,
			table1_3.three_cate_name,-- 最后一级的cate_id
			table1_3.cate_id 
		FROM
			( SELECT id, cate_name, cate_id, cate_level, parent_id FROM 1688_kj_commodity_index ) table1
			INNER JOIN (
			SELECT
				table1.cate_name two_cate_name,
				table3.cate_name three_cate_name,
				table1.parent_id two_parent_id,-- 	这个cate_id 是最后一级的cate_id
				table3.cate_id 
			FROM
				( SELECT id, cate_name, cate_id, cate_level, parent_id FROM 1688_kj_commodity_index ) table1
				INNER JOIN ( SELECT id, cate_name, cate_id, cate_level, parent_id FROM 1688_kj_commodity_index WHERE cate_id NOT IN ( SELECT parent_id FROM 1688_kj_commodity_index ) AND cate_level = 3 ) table3 ON table3.parent_id = table1.cate_id 
			) table1_3 ON table1_3.two_parent_id = table1.cate_id 
		) b 
	) table1_2_3 UNION
SELECT
	table1_2.* 
FROM
	(
	SELECT
	-- 	这个cate_id 是最后一级的cate_id
		table3.cate_id,
		table1.cate_name one_cate_name,
		table3.cate_name two_cate_name,
		'' three_cate_name
		
	FROM
		( SELECT id, cate_name, cate_id, cate_level, parent_id FROM 1688_kj_commodity_index ) table1
		INNER JOIN ( SELECT id, cate_name, cate_id, cate_level, parent_id FROM 1688_kj_commodity_index WHERE cate_id NOT IN ( SELECT parent_id FROM 1688_kj_commodity_index ) AND cate_level = 2 ) table3 ON table3.parent_id = table1.cate_id 
	) table1_2
	
	
	
	
	
	
	



```

