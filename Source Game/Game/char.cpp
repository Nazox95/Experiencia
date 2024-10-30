//Find
void CHARACTER::Initialize()
{
	CEntity::Initialize(ENTITY_CHARACTER);

	m_bNoOpenedShop = true;
  [..]

//Add in this functions
#ifdef ENABLE_EXP_TEXT
m_bShowExpText = true;
#endif
