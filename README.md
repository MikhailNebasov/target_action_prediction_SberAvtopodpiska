# ������ �� ������������ ���������� ������������� �������� �������� �� ������� ���������������� (�������������)

## 1. EDA  

[�������](https://drive.google.com/drive/folders/1rA4o6KHH-M2KMvBLHp5DZ5gioF2q7hZw) ����������� ����� ��������� ga_hits.csv � ga_sessions.csv. �������� � EDA ���������� ���������� � ����� eda.ypinb. 

## 2. Feature engeneering   

������� ����� ��������� ����������� ������ ��������������� ������. ������ ������������� OneHotEncoder() �������� � ������������� ������������� ����������� ������ � � ���� ������� ����� 100 ��. � �������� ����������� ��� ������ TargetEncoder().  

## 3. Modeling  

� �������� ������� �������������� LogisticRegression(), RandomForestClassifier(), MLPClassifier() �� ���������� scikit-learn. 

## 4. Evaluation 

LogisticRegression() - ���� 0,6353 

RandomForestClassifier() - ���� 0,6560 

MLPClassifier() - ���� 0,66 

���������� ������������������� � ������ �� ���� ������� ��������� � ��������� �����������. ��������� ��������������� ��������� �������� �������������� �������� ��� ������ �� ������. ������ ��������� ��������� ��� ����� ���������� �� MLPClassifier(). 

� ����� ��������� ����������� ������������� ����� �� ����������� ���� ������� ������� ������������ �� �����������.   

��������� ��������� ��� ��������� �� ���������� ����������� MLPClassifier(random_state=0, hidden_layer_sizes=(100, 50)) - 0,6666 

## 5. ������ 

������ ����������� ������������ ��������� ���������� � �������������� �������� ��� ������� ������������ ������. �����-��������� �� 5 ������ ����������� ����� ��� �� 20 ����� �� ������ � Ryzen 5 5600X � 16 �� ����������� ������. 

����������� ������ ������� ����� ������������ ������� ��������, ������� ������� ������ ����� � ������, � ������ ������� ����� ���������� ���������� �������� ��������� �� ��������� � ���������� ������. 

� ����� �����, ��� ������� ���������� ����� �����, ��� �������������� ��������� ���������� �������. ���������� ����� �������� ���������� ������� ��������������, ���� ���� ������ �� ��� ������, ��� �������. 

## 6. ����� 

�� ������ ������ ���� ������������� � �� �� ������ ���������� ��������� ���-������, ����������� ������ ���-�������. 

����� �������: 

eda.ypinb - ���� EDA.   

main.py - �������� ����, ����������� ���������� ������ � �� ������������. 

web.py - ����, ����������� ������ ���-�������, ����������� ����� ��������� main.py