Vim�UnDo� �V���'C��+��|��!�[�v�t�P��              :      /       /   /   /    YJ��    _�                             ����                                                                                                                                                                                                                                                                                                                                                             YJ��     �                   5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             YJ��     �               def handleRequest(req):5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             YJ��     �      	             if req == kd:5�_�                    	        ����                                                                                                                                                                                                                                                                                                                                                             YJ��     �                  5�_�                    	       ����                                                                                                                                                                                                                                                                                                                                                             YJ��     �      
   
              def kd(author):5�_�                    
       ����                                                                                                                                                                                                                                                                                                                                                             YJ��     �                 def kd(author):    �   	                          5�_�                    	       ����                                                                                                                                                                                                                                                                                                                                                             YJ��     �      
   
      def kd(author):5�_�      	              	       ����                                                                                                                                                                                                                                                                                                                                                             YJ��     �      
   
      def databaseReq(author):5�_�      
           	   	       ����                                                                                                                                                                                                                                                                                                                                                             YJ��     �         
      def databaseReq(req, author):5�_�   	              
   
       ����                                                                                                                                                                                                                                                                                                                                                             YJ�V     �   	            4    con = lite.connect('../Leaderboard/guardian.db')5�_�   
                 
       ����                                                                                                                                                                                                                                                                                                                                                             YJ�W     �   	                5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             YJ�\     �                       5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             YJ��     �                       if req == 'kills':5�_�                           ����                                                                                                                                                                                                                                                                                                                                                             YJ��     �                       5�_�                    	       ����                                                                                                                                                                                                                                                                                                                                                             YJ��     �      
         def databaseReq(req, author):5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             YJ��     �               J            cur.execute("SELECT "+author+", killDeathRatio FROM PvPTotal")5�_�                            ����                                                                                                                                                                                                                                                                                                                                                             YJ��     �                5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       YJ�     �                           cu5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       YJ�     �             �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       YJ�     �                            5�_�                       $    ����                                                                                                                                                                                                                                                                                                                                                V       YJ�"     �               >            cur.execute("SELECT killDeathRatio FROM PvPTotal")5�_�                       -    ����                                                                                                                                                                                                                                                                                                                                                V       YJ�*     �               A            return author+", your k/d ratio is: "+str(rows[0][0])5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       YJ�5     �                       if req == 'kills':5�_�                       '    ����                                                                                                                                                                                                                                                                                                                                                V       YJ�=     �               ;            return author+", your totals: "+str(rows[0][0])5�_�                       M    ����                                                                                                                                                                                                                                                                                                                                                V       YJ�D     �               M            return author+", your total number of kills is: "+str(rows[0][0])5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       YJ�I     �                        if req == 'kills total':5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       YJ�K     �                       elig 5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       YJ�U     �                           �             5�_�                           ����                                                                                                                                                                                                                                                                                                                                                V       YJ�X     �                                �                           DeathRatio5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       YJ�c     �               �               5�_�                            ����                                                                                                                                                                                                                                                                                                                                                V       YJ�d     �                            5�_�      !                  /    ����                                                                                                                                                                                                                                                                                                                                                V       YJ�i     �               5            cur.execute("SELECT kills FROM PvPTotal")5�_�       "           !      /    ����                                                                                                                                                                                                                                                                                                                                                V       YJ�i     �               4            cur.execute("SELECT kills FROM PvPTtal")5�_�   !   #           "      /    ����                                                                                                                                                                                                                                                                                                                                                V       YJ�i     �               3            cur.execute("SELECT kills FROM PvPTal")5�_�   "   $           #      /    ����                                                                                                                                                                                                                                                                                                                                                V       YJ�j     �               2            cur.execute("SELECT kills FROM PvPTl")5�_�   #   %           $      /    ����                                                                                                                                                                                                                                                                                                                                                V       YJ�k     �               1            cur.execute("SELECT kills FROM PvPT")5�_�   $   &           %      '    ����                                                                                                                                                                                                                                                                                                                                                V       YJ�p     �                 M            return author+", your total number of kills is: "+str(rows[0][0])5�_�   %   '           &          ����                                                                                                                                                                                                                                                                                                                                                V       YJ��     �                       if req == 'kd':5�_�   &   (           '          ����                                                                                                                                                                                                                                                                                                                                                V       YJ��     �               "        elif req == 'kills total':5�_�   '   )           (          ����                                                                                                                                                                                                                                                                                                                                                V       YJ��     �               $        elif req == 'kills average':5�_�   (   *           )      ,    ����                                                                                                                                                                                                                                                                                                                                                V       YJ��     �               A            return author+", your k/d ratio is: "+str(rows[0][0])5�_�   )   +           *      8    ����                                                                                                                                                                                                                                                                                                                                                V       YJ��     �               M            return author+", your total number of kills is: "+str(rows[0][0])5�_�   *   ,           +      :    ����                                                                                                                                                                                                                                                                                                                                                V       YJ��     �                 O            return author+", your average number of kills is: "+str(rows[0][0])5�_�   +   -           ,           ����                                                                                                                                                                                                                                                                                                                                                V       YJ��     �                 5�_�   ,   .           -           ����                                                                                                                                                                                                                                                                                                                                                V       YJ��     �                def handleRequest(req, author):5�_�   -   /           .          ����                                                                                                                                                                                                                                                                                                                                                V       YJ��     �                    req = req.toLower()5�_�   .               /          ����                                                                                                                                                                                                                                                                                                                                                V       YJ��    �                    if req == kd:5��