# -*- coding: utf-8 -*-

class ReadOperation(object):
	"""docstring for ReadOperation"""
	@staticmethod
	def read_common_course(tx,*students):
		"""读取Student多个实体相同的课程"""
		print(students)
		match_clause=[]
		where_clause=[]
		for i in students:
			i=i.encode("utf8")
			match_clause.append("("+i+":Student)-[:STUDY]-(c:Course)")
			where_clause.append(i+".name='"+i+"'")
		q="MATCH "+",".join(match_clause)+" WHERE "+" AND ".join(where_clause)+" RETURN c"
		print q
		res=tx.run(q).records()
		return res

		